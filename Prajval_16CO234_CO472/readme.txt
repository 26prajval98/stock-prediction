1. Should have python 3 with jupyter notebook

2. The following are the contents

	- code folder contains 2 files:
		* GRU_model.ipynb which is the GRU model
		* GRU_model.ipynb which is the LSTM model
		It also contains scripts folder which has code to generate new dataset. Refer point 4.
	
	- dataset folder contains the complete dataset
	
	- screenshots folder contains execution screenshots
	
	- readme.txt file contains the steps to reproduce the paper and the contents of this project

	- Plagiarism Report.pdf contains the plagiarism percentage which is 8%. This was obtained using the software Plagiarism Checker X

	- Report_Prajval_16CO234_CO472.docx contains the report in word format.
	
	- Report_Prajval_16CO234_CO472.pdf just in case .docx file does not open
	
	The last point is very important. Go through it before going through the others.


3. To run the code you need to install all the following dependencies:
	
	- numpy
	
	- pandas
	
	- scikit learn
	
	- keras
	
	- tweep

4. The complete dataset used is the folder dataset. To regenerate the dataset go to the directory code/scripts and run the file tweets_to_csv.py as py tweets_to_csv.py. However before you can run the script you have to get twitter consumer secret and key by applying it here: https://developer.twitter.com/en/apply-for-access

5. Keeping the same directory format to execute the code open the jupyter notebook file and execute is cell by cell. If vscode is installed vscode can detect it.

6. If you are changing the directory update the dataset path in the following line:
	dataset = pd.read_csv('../dataset/IBM_with_twitterscore.csv', index_col='Date', parse_dates=['Date'])
../dataset/IBM_with_twitterscore.csv represents path to the dataset file.

7. If all this is a hastle you can login to kaggle.com and import the jupyter notebook in kaggle itself and run it then and there. However you will have to upload the dataset and change path as per point 4. This is the most easiest and suggest method as there is no need to install any dependencies.
