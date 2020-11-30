[![Build Status](https://travis-ci.com/terencecistudent/peter-photography.svg?branch=master)](https://travis-ci.com/terencecistudent/peter-photography)

# Peter Lynch Photography

## Description
This is a photo gallery website that displays photographs taken by a friend of mines.  Images are displayed in rows of 4 with continuous columns.  Users are able to hover over and click on an image to bring up a larger version of the image.  Users can scroll through the images by pressing either the right and left arrows, or by clicking on the arrows on each side of the image.  The photographer's social media profiles are connected to icons at the top of the page.

## Wireframes
To complete...

## UX
### User Stories
#### Implemented:
1. As a user, I would like to see the images displayed in a nice format.
    - **End User Goal**: User is able to upload the website with the styles being applied for the images to be displayed nicely.
    - **End Business Goal**: Images displaying in a nice format.
    - **Acceptance Criteria**: Images displaying in a nice format due to the styles from the stylesheet.
    - **Measures Of Success**: Check Manual Tests.

2. As a user, I would like to click on an image which will then bring up a bigger version of that image.
    - **End User Goal**: User is able to click on any image which will then show a bigger version of that image.
    - **End Business Goal**: Images to be displayed in a larger format when clicked on.
    - **Acceptance Criteria**: Images to be displayed in a larger format when clicked on.
    - **Measures Of Success**: User is able to clock on an image which then brings up a bigger version of that image.  Check Manual Tests.

3. As a user, I would like to scroll through the images.
    - **End User Goal**: User is able to scroll through all of the images.
    - **End Business Goal**: Users are able to scroll through all of the images.
    - **Acceptance Criteria**: Users are able to scroll through all of the images.
    - **Measures Of Success**: User is able to scroll through the images.  Check Manual Tests.

4. As a user, I would like to X off the bigger version of an image that I clicked on.
    - **End User Goal**: User is able to X off a particular or any image by clicking the X icon below the image.
    - **End Business Goal**: Users to have simple navigation to X off an image by clicking on the X icon below the image.
    - **Acceptance Criteria**: Users to be able to click off an image using the X icon.
    - **Measures Of Success**: User is able to click off the image by pressing the X icon.  Check Manual Tests.

5. As a user, I would like to click on any of the social media icons where I should be directed to that social media page.
    - **End User Goal**: User is able to click on any social media icon which directs them to the correct page.
    - **End Business Goal**: Users are able to click on any of the social media icons where they are directed to the correct pages.
    - **Acceptance Criteria**: Users are able to click on any of the social media icons where they are directed to the correct pages.
    - **Measures Of Success**: User is directed to the correct social media pages.

## Framework
For the styling side of the website, I have decided to use Bootstrap 4.  As Bootstrap is a mobile first framework, this is suitable for my website as users do not need to be on a laptop or computer to see the website properly.  Users can view the website using their mobiles and still access the images.

I have used the Django framework as I have used the language Python. Although it could be argued that Flask may be the more suitable framework for this type of website.  I felt that in the case, that if the client wanted to expand upon his website, then Django could make future implementations easier with the likes of Django forms and models.

## Requirements
- Access to a desktop, laptop, tablet and mobile devices.
- Internet connection.

## Features
- **Images**: Users can click and scroll through the images.
- **Social Media Icons**: Users can click on any of the social media icons which directs them to a social media profile page.

## Database Schema
### Development:
During development, I have used Django's SQLite3 database.

**Setting Up SQLite3:**

- When your Django app is started up, in the terminal run py manage.py migrate as such:
![image](https://user-images.githubusercontent.com/48124466/100473602-aa1b9100-30d6-11eb-846d-b6fd0a5dda44.png)

- This will then create an SQLite3 Database:
![image](https://user-images.githubusercontent.com/48124466/100473687-d6371200-30d6-11eb-9764-b0a47f3f6179.png)

- If you create models in the models.py file, in the terminal run **py manage.py makemigrations** which will created the model.  After that run **py manage.py migrate** which will migrate the changes to the SQLite3 Database.

### Production:
During production, I have used Heroku Postgres.

### Setting It Up In Heroku
- Once in the app in Heroku, go to resources, find **Add-ons** and search for Heroku Postgres:
![image](https://user-images.githubusercontent.com/48124466/80263198-c4e0df80-8687-11ea-9910-326c645c6b9d.png)

- Click on Heroku Postgres, Plan name: Hobby Dev - Free:
![image](https://user-images.githubusercontent.com/48124466/80263413-74b64d00-8688-11ea-9f53-ea139c6ea2a9.png)

- It is now attached as a database:
![image](https://user-images.githubusercontent.com/48124466/80263452-99122980-8688-11ea-8e90-8194a95e424e.png)

- Go to Settings > Reveal Config Vars:
![image](https://user-images.githubusercontent.com/48124466/80263619-15a50800-8689-11ea-960c-fb93d9593184.png)

### Connecting Database to VS Code:
- In the terminal, run:
    - pip install dj-database-url
    - pip install psycopg2

- Import dj_database_url in the settings.py file.

- In settings.py, add dj_database_url to databases (I have used an env variable to store my DATABASE_URL):
![image](https://user-images.githubusercontent.com/48124466/80264126-ef806780-868a-11ea-8c23-184d0e3d30e2.png)

- In the terminal:
    - run py manage.py makemigrations
    - run py manage.py migrate
        - This migrates all existing migrations to the new Postgres database.
    - run py manage.py createsuperuser and fill out the details.
    - The SQLite database which ran locally on your own machine was used for testing. You will have to rebuild your items in the new production database.

## AWS S3 Buckets
### Setting It Up:
- Go to [AWS](https://aws.amazon.com/) and create an account or sign in.

- Go to Management Console > S3 > Properties > Static website hosting:
    ![image](https://user-images.githubusercontent.com/48124466/100555472-95d0c300-3293-11eb-87f0-6995c548ae7c.png)

- Go to Permissions > CORS Config:
    - Add new cors configuration.
    ![image](https://user-images.githubusercontent.com/48124466/100555511-e9431100-3293-11eb-89fb-43b8fd19521f.png)

- Go to Permissions > Bucket Policy:
    - Add a new policy here.
    ![image](https://user-images.githubusercontent.com/48124466/100555549-2c9d7f80-3294-11eb-8aa4-7658abd20cab.png)

- Go to IAM > Groups:
    - Create New Group.
    ![image](https://user-images.githubusercontent.com/48124466/100555588-5ce51e00-3294-11eb-9b5a-2e4f68fd0bc8.png)

- Go to IAM > Policies:
    - Select JSON and create policy.
    ![image](https://user-images.githubusercontent.com/48124466/100555634-afbed580-3294-11eb-89b5-8de5422e1537.png)

- Now the policy is made, need to add it to the group that was made earlier:
    - Go to IAM > Groups.
    - Permissions > Attach Policy and attach policy created.
    ![image](https://user-images.githubusercontent.com/48124466/100555659-e4329180-3294-11eb-8c38-6fa6201b9802.png)

- Go to IAM > Users:
    - Add User
    - Access type: Turn Programmatic access on.
    ![image](https://user-images.githubusercontent.com/48124466/100555696-2d82e100-3295-11eb-9f65-a1f3f4651b8f.png)

- Choose Group that was created:
    ![image](https://user-images.githubusercontent.com/48124466/100555720-56a37180-3295-11eb-85ea-83b9eba26c9c.png)

- Once that is done, you will get this message.  Download and store Excel file carefully as it contains your keys
    needed in your software.
    ![image](https://user-images.githubusercontent.com/48124466/80267086-4a1fc080-8697-11ea-88cd-1648415d00e3.png)

### Adding S3 To Django:
- In the terminal, run:
    - pip install django-storages
    - pip install boto3
    - Both of these are packages that will allow you to connect Django to S3.

- In settings.py, add **storages** to INSTALLED_APPS:
    ![image](https://user-images.githubusercontent.com/48124466/100555805-ecd79780-3295-11eb-90ca-731929db03de.png)

- In settings.py, add a setting in which will keep static files from expiring e.g.
    ![image](https://user-images.githubusercontent.com/48124466/80267379-6d973b00-8698-11ea-938e-4e79efe77ebd.png)

- In settings.py, you need to put in the AWS storage bucket name that you created in S3.
- Need to write which region you have used.
- You get your AWS access key and secret key from your environment variables e.g.
    ![image](https://user-images.githubusercontent.com/48124466/100555890-5eafe100-3296-11eb-967e-5b25bdf3124b.png)

- The domain that you can use is something as follows, where your AWS Storage bucket 
    name is injected in there:
    ![image](https://user-images.githubusercontent.com/48124466/80267526-6c1a4280-8699-11ea-82ac-ba8d018555d5.png)

- You will have to tell it that the static file storage is storages:
    ![image](https://user-images.githubusercontent.com/48124466/80267557-86ecb700-8699-11ea-82b7-dc87915ff6d8.png)

- In the terminal, run:
    - py manage.py collectstatic
    - This will transfer the static folder into S3.

### Adding Media to S3
- This is a way of storing media files as well as static files on S3.

- Use STATICFILES_LOCATION from settings.py as the location.
    ![image](https://user-images.githubusercontent.com/48124466/80269142-f7e59c00-86a4-11ea-9539-b4a55d4d3909.png)

- In settings.py, add STATICFILES_LOCATION and give it a value 'static'.

- Change STATICFILES_STORAGE to custom_storages.StaticStorage.
    ![image](https://user-images.githubusercontent.com/48124466/80269268-14ce9f00-86a6-11ea-8dd7-fff076fee14d.png)

- In the terminal, run:
    - py manage.py collectstatic
    - This will put a static directory in S3.

- Refresh S3 Bucket.

- In settings.py, MEDIAFILES_LOCATION will be media.
- DEFAULT_FILE_STORAGE will refer to the custom storages.py.
    ![image](https://user-images.githubusercontent.com/48124466/80269331-bce46800-86a6-11ea-9992-ca8003351062.png)

## Deployment
This application was deployed using Heroku which can be viewed from here: [Peter Lynch Photography](https://peterlynch-photograph.herokuapp.com)

I have used VS Code to help develop this website. This was pushed to Heroku through the command line by linking the master git from my remote GitHub repository to a new app created in Heroku.

There are no differences between the website's development version and the deployed version to Heroku.

### Deploying to Heroku:
1. Go to the Heroku website [here](https://id.heroku.com/login).

2. Sign Up or Sign In which will direct you to the dashboard.

3. Click on **New > Create new app**.

4. Enter app name and choose region then press **Create App**.

5. Go to **Settings > Reveal Config Vars**:
    - Enter Keys and their values, example keys below:
    ![image](https://user-images.githubusercontent.com/48124466/100556565-1cd56980-329b-11eb-9d71-13152bc4a338.png)

6. In the CLI, login into Heroku by **heroku login -i**, where you will be asked to your enter email address and password.

7. If you have already created your Heroku app, you can remote to your local repository with the heroku git:remote command.

8. Set debug=False for deployment.

9. To deploy your app to Heroku, use the git push command to push the code from your local repository’s master branch to 
    your heroku remote:
    ![image](https://user-images.githubusercontent.com/48124466/76408974-ae0b5580-6385-11ea-9cf1-8d67c4f0dff5.png)

10. When the build is complete, on the Heroku website, in the app click **Open App**.

[Deploying with Git](https://devcenter.heroku.com/articles/git)

## Testing
### Travis CI
At the top of this document, you will see Travis in action.
It is a hosted continuous integration service used to build and test software projects.

### Manual Tests:
I have carried out manual tests on User Stories No. 1-4.

[Manual Tests](https://github.com/terencecistudent/peter-photography/blob/master/Manual%20Tests.pdf)

### Responsiveness On Different Devices Tests:
[Responsive Tests](https://github.com/terencecistudent/peter-photography/blob/master/Website%20Responsive%20Sizes.pdf)

### Running Responsive Designs on Google Chrome:
Here is a link how to run the application on a live server by configuring and exposing ports with GitPod:
https://www.gitpod.io/docs/43_config_ports/

**To view responsive applications:**
1. Right click then go to **Inspect Element**.
2. Click on the **Toggle Device Toolbar** (Icons showing two devices):
    ![image](https://user-images.githubusercontent.com/48124466/68051275-f2ebf500-fcde-11e9-8b3a-adc7abc16c5f.png)
3. Click on any device, for example, iPhone 5/SE selected:
    ![image](https://user-images.githubusercontent.com/48124466/68051467-5aa24000-fcdf-11e9-8666-d29f1afa8955.png)

### Code Validation
- HTML
    - is validated using [W3 validator](https://validator.w3.org/).
- CSS
    - is validated using [W3 Jigsaw](https://jigsaw.w3.org/css-validator/).
- Python
    - is validated using [Pep8Online](http://pep8online.com/).

## Technologies Used
### Languages:
- HTML5
    - Used for the structure and layout.
- CSS3
    - Used for the styling of the wesbsite.
- JavaScript
    - Used to implement lightbox structure.
- Python
    - Used to code the back end functions.

### README.md:
- Markdown
    - Used for the README.md file.

### Frameworks:
- Bootstrap v4.3.1
    - This framework is used in this appplication for:
        - Navbar
        - Styling
        - Responsive Layouts
        - Image Layouts
- Django Framework v3.1.3
    - Is a Python framework that encourages rapid development.

### Databases:
**Development**
- SQLite3
    - Is Django's standard SQL Database.

**Production**
- Heroku Postgres
    - PostgreSQL used to link tables together.

### Libraries:
- Font Awesome
    - Font Awesome Icons were used throughout the website.
- jQuery
    - Used to help simplify HTML DOM tree traversal and manipulation.
- Google Fonts
    - Helped with the visibility of the text for users to see clearly.

### Others:
- Git 
    - Version control to the GitHub repositories.
    - Ran the code to expose a live port.
- GitHub
    - Remote repository.
- Google Chrome Developer Tools 
    - Helped with small changes.

## Cloning and Pushing To The Respository
### Cloning:
- Here is a link how to clone a repository: 
https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository

### Pushing To The Respository:
- To add, commit and push files to the repository, e.g. index.html, open a New Terminal and type:
1. git add index.html
2. git commit -m "Leave a message here"
3. git push origin master - (which is for the master branch).

- To create a new branch within your current application, open a New Terminal:
1. Create a branch: git checkout -b new-branch-name
2. Edit, add to your application and commit the files.
3. Push the branch to the remote repository: git push origin new-branch-name.

## Support
To contact GitHub, follow this link: https://support.github.com/

### Author:
- Terence Logue
