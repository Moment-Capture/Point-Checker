
from path import *
from utils import *
from recognize import *

def main():
    # upload 폴더 생성
    makeFolder(UPLOAD_FOLDER)

    # 경로 정의
    client_id = "test"
    id_path = UPLOAD_FOLDER + "\\" + client_id
    pdf_path = "D:\\Dropbox\\Dropbox\\[대학]\\졸업 프로젝트\\캡스톤 그로스\\테스트파일\\5_test_135710.pdf"
    path = str(Path(id_path))
    jpg_path = path + "\\" + "jpg"

    # 파일 생성
    makeIdFolder(path)
    print(pdf_path)
    print("test 폴더 생성 완료")
    
    # pdf 파일 탐지
    original_pdf_file_path_list = []
    original_pdf_file_path_list.append(pdf_path)
    
    # pdf 파일 jpg로 변환
    convertPdfToJpg(original_pdf_file_path_list, jpg_path)

    # jpg 파일 개수 검사
    jpg_file_path_list = []
    jpg_file_path_list = os_sorted(Path(jpg_path).glob('*.jpg'))

    # jpg에 적힌 코드 인식해서 testee 구분
    testee_jpg_df = pd.DataFrame(columns=["index_id", "file", "testee_id", "page"])
    id_match = pd.DataFrame(columns=["testee_id", "testee_name"])
    testee_jpg_df, id_match = testeeCodeRecognition(jpg_file_path_list, testee_jpg_df)

    print()
    print(id_match)

    print()
    print("finish")

    deleteFolder(id_path)


main()