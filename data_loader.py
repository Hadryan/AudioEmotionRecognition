import librosaimport numpy as npfrom sklearn.model_selection import train_test_splitdef data_loader():    fp = open('PathLabel.txt', 'r')    files_Namelist = fp.read().split('\n')[:-1]    y_train = []    mfcc = []    for idx, path in enumerate(files_Namelist):        percent = float(idx) * 100 / len(files_Namelist)        if percent % 10==0:            print('Loading data: '+ str(percent)+'%')        [file_path, label] = path.split(' ')        X, sample_rate = librosa.load(file_path                                      , res_type='kaiser_fast'                                      , duration=2.5                                      , sr=44100                                      , offset=0.5                                      )        sample_rate = np.array(sample_rate)        mfccs = np.mean(librosa.feature.mfcc(y=X,                                             sr=sample_rate,                                             n_mfcc=13),                        axis=0)        if mfccs.shape[0] !=216:            print(idx+1)            print(mfccs.shape[0])            continue        mfcc.append(mfccs)        y_train.append(label)    mfcc = np.array(mfcc)    y_train = np.array(y_train).reshape(-1, 1)    x_train, x_test, y_train, y_test = train_test_split(mfcc, y_train, test_size=0.2, random_state=42)    print('Data confirmed!')    return x_train, x_test, y_train, y_test# if __name__ == '__main__':#     x_train, x_test, y_train, y_test =  data_loader()