import requests

# bắt các request khi  đăg nhập vào trang
url = 'https://autoitvn.com/'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'cookie': '__gads=ID=171d41ba48d8385a-22846f7949ca00a0:T=1625981069:RT=1625981069:S=ALNI_MYQjhTrkzAoeNOvm8b6pnvb3QQOuw; G_ENABLED_IDPS=google; xf_user=18199%2Cb31fe9036abec9ead2a56e50da404b93c6d5ca44; xf_session=abe2f7a3762db38ebf4ef3a29d060bc2'
}
res = requests.get(url,headers=headers)
#status_code = res.status_code
data = res.text
print(data)


# requests để login vào trang

url = 'https://autoitvn.com/login'
headers_login = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'cookie': '__gads=ID=171d41ba48d8385a-22846f7949ca00a0:T=1625981069:RT=1625981069:S=ALNI_MYQjhTrkzAoeNOvm8b6pnvb3QQOuw; G_ENABLED_IDPS=google; xf_user=18199%2Cb31fe9036abec9ead2a56e50da404b93c6d5ca44; xf_session=abe2f7a3762db38ebf4ef3a29d060bc2'
}
values = {'username': 'loonazs998@gmail.com',
          'password': '1581998ltnQ'}

r = requests.post(url, data=values,headers=headers_login)
show = r.text
print(show)

