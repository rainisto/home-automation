import sys
import argparse


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib

import config
from container import Container
from model.DataSource import DataSource


argparse = argparse.ArgumentParser()
argparse.add_argument("-d", "--days-behind", required=True, dest="days_behind", type=int,
                      help="Days behind to be taken into account")
argparse.add_argument("-p", "--test-file-percent", required=True, dest="test_file_percent", type=int,
                      help="Percent of the data that will be generated into a separate test file")
argparse.add_argument("-dp", "--datapoints-behind", required=True, dest="datapoints_behind", type=int,
                      help="Datapoints behind to be added for the model on each line")
argparse.add_argument("-hg", "--hour-granularity", required=True, dest="hour_granularity", type=int,
                      help="How many hours a datapoint will agregate")
argparse.add_argument("-ds", "--data-source", required=False, dest="data_source", type=str,
                      default=DataSource.WEATHER_STATION.value,
                      help="What datasource to use: weather station or darksky")
argparse.add_argument('--grid-search', dest='grid_search', action='store_true')
args = vars(argparse.parse_args())

container = Container()
dataframe = container.prepared_data_provider().get(args['days_behind'], args['datapoints_behind'],
                                                   args['hour_granularity'], args['data_source'])
main_data, test_data = train_test_split(dataframe, test_size=args['test_file_percent'] / 100)

dataframe.to_csv('sample_data/all.csv')
main_data.to_csv('sample_data/training_data.csv')
test_data.to_csv(config.model['test_data_file'])

X = main_data.iloc[:, 1:].values
y = main_data.iloc[:, 0].values
scaler = StandardScaler()
X = scaler.fit_transform(X)

if args['grid_search']:
    print(container.keras_grid_search().search(X, y))
    sys.exit()

model_builder = container.keras_model_builder()
classifier = model_builder.build(X.shape[1], 'adam', 0.2)
classifier.fit(X, y, batch_size=2, epochs=50)

classifier.save(config.model['keras_model_file_name'])
joblib.dump(scaler, config.model['sklearn_scaler_file_name'])