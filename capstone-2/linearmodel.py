# from sklearn.preprocessing import MinMaxScaler
# import numpy as np
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error, r2_score
# from sklearn.preprocessing import StandardScaler
# import pickle
# df=pd.read_csv("niftydata20yrs.csv")
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error, r2_score
# from sklearn.preprocessing import StandardScaler

# # Assuming 'df' is your DataFrame containing the dataset
# data = {
#     'Year': df['Year'],
#     'Jan': df['Jan'],
#     'Feb': df['Feb'],
#     'Mar': df['Mar'],
#     'Apr': df['Apr'],
#     'May': df['May'],
#     'Jun': df['Jun'],
#     'Jul': df['Jul'],
#     'Aug': df['Aug'],
#     'Sep': df['Sep'],
#     'Oct': df['Oct'],
#     'Nov': df['Nov'],
#     'Dec': df['Dec'],
#     'Annual': df['Annual']
# }

# # Convert to DataFrame
# data_df = pd.DataFrame(data)

# # Separate features and target variable
# X = data_df.iloc[:, :-1].values  # Features
# y = data_df.iloc[:, -1].values   # Target variable

# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=27)

# # Standardize the features (optional but recommended)
# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)

# # Create and train the linear regression model
# model = LinearRegression()
# model.fit(X_train, y_train)
# filename = 'digital_eye.pkl'
# pickle.dump(model, open(filename, 'wb'))

#  # Make predictions on the test set
# # y_pred = model.predict(X_test)

# # # Evaluate the model
# # mse = mean_squared_error(y_test, y_pred)
# # r2 = r2_score(y_test, y_pred)


# # print("Mean Squared Error:", mse)
# # print("R^2 Score:", r2)


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import pandas as pd
import pickle

# Load the dataset
df = pd.read_csv("niftydata20yrs.csv")

# Assuming 'df' is your DataFrame containing the dataset
# data2 = {
#     'Annual': df['Annual']
# }
# data1= {
#     'Jan': df['Jan'],
#     'Feb': df['Feb'],
#     'Mar': df['Mar'],
#     'Apr': df['Apr'],
#     'May': df['May'],
#     'Jun': df['Jun'],
#     'Jul': df['Jul'],
#     'Aug': df['Aug'],
#     'Sep': df['Sep'],
#     'Oct': df['Oct'],
#     'Nov': df['Nov'],
#     'Dec': df['Dec'],
# }

# # Convert to DataFrame
# data_df1 = pd.DataFrame(data1)
# data_df2 = pd.DataFrame(data2)
# X = data_df1
# y = data_df2

# # Create and train the linear regression model
# model = LinearRegression()
# model.fit(X, y)
# filename = 'linearmodel.pkl'
# pickle.dump(model, open(filename, 'wb'))
# Load the dataset
# df = pd.read_csv("niftydata20yrs.csv")

# # Combine features and target into a single dataframe
# data = df[['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Annual']]

# # Separate features and target variable
# X = data.iloc[:, :-1]  # Features
# y = data['Annual']     # Target variable

# # Create and train the linear regression model
# model = LinearRegression()
# model.fit(X, y)

# # Save the trained model
# filename = 'linearmodel.pkl'
# pickle.dump(model, open(filename, 'wb'))




import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# Load the dataset
df = pd.read_csv("niftydata20yrs.csv")

# Separate features and target variable
X = df[['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']]
y = df['Annual']

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_scaled, y)

# Save the trained model and scaler
filename_model = 'linearmodel.pkl'
filename_scaler = 'scaler.pkl'
pickle.dump(model, open(filename_model, 'wb'))
pickle.dump(scaler, open(filename_scaler, 'wb'))
