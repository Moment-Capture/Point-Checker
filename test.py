
from path import *
from utils import *
from recognize import *
from pointchecker import getMulSubDf


# 경로 정의
client_id = "test"
id_path = UPLOAD_FOLDER + "\\" + client_id
path = str(Path(id_path))
jpg_path = path + "\\" + "jpg"
temp_path = path + "\\" + "temp"


def make_test_dir():
    file_path = input("파일 이름을 입력해주세요: ")
    pdf_path = "D:\\Dropbox\\Dropbox\\[대학]\\졸업 프로젝트\\캡스톤 그로스\\최종 데모" + "\\" + file_path
    print(pdf_path)
    
    # upload 폴더 생성
    makeFolder(UPLOAD_FOLDER)

    # 폴더 생성
    makeFolder(path)
    makeFolder(jpg_path)
    makeFolder(jpg_path + "\\" + "mul")
    makeFolder(jpg_path + "\\" + "sub")
    print("test 폴더 생성 완료")

    # pdf 파일 탐지
    original_pdf_file_path_list = []
    original_pdf_file_path_list.append(pdf_path)
    
    # pdf 파일 jpg로 변환
    convertPdfToJpg(original_pdf_file_path_list, jpg_path)

    # jpg 파일 개수 검사
    jpg_file_path_list = []
    jpg_file_path_list = os_sorted(Path(jpg_path).glob('*.jpg'))

    return jpg_file_path_list


def id_detect_check():
    jpg_file_path_list = make_test_dir()

    # jpg에 적힌 코드 인식해서 testee 구분
    testee_jpg_df = pd.DataFrame(columns=["index_id", "file", "testee_id", "page"])
    id_match = pd.DataFrame(columns=["testee_id", "testee_name"])
    testee_jpg_df, id_match = testeeCodeRecognition(jpg_file_path_list, testee_jpg_df)

    print()
    print(id_match)

    print()
    print("finish")

    deleteFolder(id_path)


def exception_check():
    jpg_file_path_list = make_test_dir()
    total_qna_num = input("총 문항 수를 입력해 주세요: ")

    testee_df = getMulSubDf(jpg_path, total_qna_num)

    testee_df = fillOneDf(testee_df)

    print()
    print_full(testee_df)


exception_check()