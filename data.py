import os
import time
import pandas as pd

from pathlib import Path
from natsort import os_sorted

from pointchecker import pointchecker
from path import *
from utils import *


ALLOWED_FILE_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_FILE_EXTENSIONS


def getJsonData(client_id, data, files):
    ## upload 폴더 생성 ##
    try:
        if not os.path.exists(UPLOAD_FOLDER):
            os.mkdir(UPLOAD_FOLDER)
    except:
        pass
    ## upload 폴더 생성 ##

    id_path = UPLOAD_FOLDER + "/" + client_id

    print(client_id)
    print(id_path)

    ## id 폴더 생성 ##
    try:
        if not os.path.exists(id_path):
            os.mkdir(id_path)
    except:
        pass
    ## id 폴더 생성 ##

    pdf = files["pdf"]
    pdf_name = pdf.filename
    pdf_path = os.path.join(id_path, pdf_name)
    if pdf and allowed_file(pdf_name):
        pdf.save(pdf_path)
    
    test_name = data["test_name"]
    copy_num = data["copy_num"]
    total_qna_num = data["total_qna_num"]
    testee_num = data["testee_num"]
    test_category = data["test_category"]
        
    print("파일 업로드 성공")

    plural_check(id_path, test_name, copy_num, total_qna_num, testee_num, test_category)

def plural_check(id_path, test_name, copy_num, total_qna_num, testee_num, test_category):
    start = time.time()
    df = pd.DataFrame()
    df = pointchecker(id_path, test_name, copy_num, total_qna_num, testee_num, test_category)
    end = time.time()
    point_eta = end - start

    print()
    print(df.set_index(keys=["testee_id", "file"], drop=True))
    print()
    print("point_eta: " + f"{point_eta:.2f} sec")
    
    if len(df) == 0:
        return "Error Occured", 200
    
    json_data = df.to_json(orient="records")

    return json_data