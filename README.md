
# Welcome to your CDK Python project!

This is a blank project for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

## Lab Process Screen shots
1. synthesizing CloudFormation template
![alt text](<Screenshot from 2024-11-18 09-33-25.png>)
![alt text](<Screenshot from 2024-11-18 09-33-43.png>)

2. deploying for the s3 bucket
![alt text](<Screenshot from 2024-11-18 09-35-30.png>)
![alt text](<Screenshot from 2024-11-18 09-37-04.png>)
![alt text](<Screenshot from 2024-11-18 09-39-07.png>)

3. added the remaining functions (ec2 and vpc) and synthesizing them
![alt text](<Screenshot from 2024-11-18 09-51-06.png>)
![alt text](<Screenshot from 2024-11-18 09-51-55.png>)
![alt text](<Screenshot from 2024-11-18 09-53-07.png>)
![alt text](<Screenshot from 2024-11-18 09-53-23.png>)

4. deploying all (ec3,vpc and s3)
![alt text](<Screenshot from 2024-11-18 09-54-41.png>)
![alt text](<Screenshot from 2024-11-18 09-54-56.png>)
![alt text](<Screenshot from 2024-11-18 09-55-17.png>)

5. deployment completed 
![alt text](<Screenshot from 2024-11-18 09-59-30.png>)