from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    
    def on_start(self):
        response = self.client.post('/accounts/api/v1/jwt/create/',
                                     data={'email':'admin@admin.com',
                                           'password':'1234'}).json()
        self.client.headers = {'Authorization': f'Bearer {response.get("access", None)}'}

    @task
    def api_task_list(self):
        self.client.get('/api/v1/task/')
    @task
    def api_task_list(self):
        self.client.get('/api/v1/task/1/')