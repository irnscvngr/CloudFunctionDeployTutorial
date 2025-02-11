import functions_framework

# This is just a second hello_world_function to test:
# can a new cloud-function be created directly by deploying from GitHub
@functions_framework.http
def hello_world_2(request):  # This is your Cloud Function
    return "Hello World! This function was directly created in GitHub.", 200