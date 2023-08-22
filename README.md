# Tek_News

## Setup
Create a .env file in root of project .
DB_USER and DB_PASSWORD are required in .env file. Also put a secure secret key too, otherwise django insecure key will be used.
<br><br>Run this command and create your database in docker .<br>
 `docker exec -it <>DB_contatiner_name mysql -u <DB_username> -p`<br>

## Run
<b>make sure that you have access to chromedriver site because of filtering<br><br></b>
`docker-compose build`<br>
`docker-compose up`<br><br>
if you had any possible problem on process you can restart backend service by`docker-compose restart backend`
### for search:
go to this URL `http://localhost:8000/api/news?search=< word you want to search>`
#### search by fields:
go to this URL `http://localhost:8000/api/news?search=<fields name like title , tags> : < word you want to search>`
#### search with multiple  terms:
got to this URL `http://localhost:8000/api/news?search=< word you want to search>&search=<another word you want to search too>`

## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://gitlab.roshan-ai.ir/ehsan-moslemi/tek_news.git
git branch -M main
git push -uf origin main
```

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/index.html)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing(SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)

***


