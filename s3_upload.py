import boto3
import os # 현재 업로드할 파일 탐색

def upload_files(search_path, target_path):
   session = boto3.Session(
       aws_access_key_id='AKIAZR3IWTCZWC4AV645',
       aws_secret_access_key='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',
       region_name='ap-northeast-2'
   )

   s3 = session.resource('s3')
   bucket = s3.Bucket('media.wpsshool.site')

   for current_dir, subdir, files in os.walk(search_path):
       for file in files:
           full_path = os.path.join(current_dir, file)
           # print(full_path)
           # print(full_path.replace("\\","/")[len(search_path)+1:])
           with open(full_path, 'rb') as data: # rb - binary 형태
               bucket.put_object(Key=target_path+"/"+(full_path.replace("\\","/"))[len(search_path)+1:],Body=data, ACL='public-read')
               # Key는 media 하위에 올릴 것이다.(s3에 올라갈 폴더) 윈도우에서는 하위 경로를 \\로 표시하므로, /로 바꿔준다.
if __name__ == "__main__":
   upload_files('./media', 'media')

