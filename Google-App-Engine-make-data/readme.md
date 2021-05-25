# How to deploy PyWebIO apps on [Google App Engine](https://cloud.google.com/appengine)

### NOTE about cost: This deployment option is NOT FREE. It will incur small cost (on the order of $0.05-0.1/hour) continuously in your Google Cloud Billing account.

## Step 1
Go to [App Engine homepage](https://cloud.google.com/appengine) and click on **"Go to Console"**.

## Stpe 2

- On top right corner there should be button for **"Activate Cloud Shell"**. Click on that to work using the Cloud Shell. [Cloud Shell is an online development and operations environment](https://cloud.google.com/shell) accessible anywhere with your browser. You can manage your resources with its online terminal preloaded with utilities such as the gcloud command-line tool, kubectl, and more.

- There should also be button **"Learn"** near top right corner. Click on it to open up the tutorials menu.

- Choose the very first option **"App Engine Quickstart"**.

- Look for the **"Python"** link under the second group **"Flexible environment"** and click on it (the first group is **"Standard environment"**).

## Step 3

- Go to the step 2 of the GCP tutorial (NOT step 2 of this Readme file) and do the cloning as instructed in the first step. Note, this command (and all the following ones) will be executed on the Cloud Shell terminal.

`git clone https://github.com/GoogleCloudPlatform/python-docs-samples`

- Instead of going to the `hello_world` directory (as instructed in the tutorial), create a new PyWebIO (or your app-name) directory under `python-docs-samples/appengine/flexible` i.e.

`mkdir python-docs-samples/appengine/flexible/pywebio`

- Copy/create/git clone all the three files of this Github directory (`app.yaml`, `main.py`, and `requirements.txt`) into this `pywebio` directory. You can even fire up an Cloud Shell Editor and copy-paste the contents of the file just like a text editing task.

## Step 4
- You can do a local test of your app by,

  - `virtualenv env`
  - `source env/bin/activate`
  - `python3 main.py`

This should fire up your Flask app and run a web server on Port 8080. 

- There should be a small (human eye) icon on the Cloud Shell window frame called **"Web preview"**. This will open a browser page with port 8080 (by default) which should show your app and you should be able to interact with it just as expected. All of these is described in the Step 4 of the GCP tutorial too.

## Step 5

Go to Step 5 of the GCP tutorial and follow along

- Execute `gcloud app create` on the Cloud shell (making sure you are still in the `pywebio` directory)
- Execute `gcloud app deploy` on the Cloud shell.

**That's it!** You have to enter 'Y' on the Cloud Shell terminal for the deployment process and then the magic will happen. Sit back and relax as the deployment in this Flexible environment takes at least a few minutes because it spins up a dedicated VM instance, creates Kubernetes cluster with Docker, installas all your supporting libraries, establishes the runtime, and then deploy the app i.e. start a web server.

## What's the app URL?

The URL for your app should be visible fron the Step 5 of the GCP tutorial. They will list it at the bottom of the page. Also, the link should be there on the **'Dashboard'** page of the App Engine Console. You can distribute this URL to anybody in the world now!

