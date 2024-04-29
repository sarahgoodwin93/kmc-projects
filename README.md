# [KMC Projects](https://kmc-projects-686d2f98b9c9.herokuapp.com/ "KMC Projects deployed site")

![am-i-responsive-image](media/README-images/am-i-responsive.png "am-i-responsive-image")

- Introduction
- [Live Site Link](https://kmc-projects-686d2f98b9c9.herokuapp.com/ "KMC Projects deployed site")

KMC Projects is a real world business founded by Kevin McCaffrey. The site has been created to showcase the work and serives that KMC Projects provides, offer an easy contact for clients to get in touch, and a database of products that KMC Projects distributes that clients can purchase. 

KMC Projects offers a comprehensive range of services tailored to meet the diverse needs of commercial companies in the hydraulic industry. From hydraulic design and consultancy to project management and training, they are dedicated to delivering innovative solutions that ensure precision, efficiency, and success.

They provide a distribution list of hydraulic products. Whether you're sourcing components for a new project or replacing parts in existing systems, our inventory ensures that you have access to top-quality products that meet your requirements.

Throughout this README both KMC Projects and Kevin McCaffrey will be referred to as 'the client'.

## Table of Contents

- [Key Project Goals](#key-project-goals)
- [Business Model](#business-model)
- [Agile Development](#agile-development)
- [User Stories](#user-stories)
    - Epic
    - Future Stories
- [User Experience](#user-experience)
    - Wireframes
    - Database Schema
    - Typography
    - Colour Palette
    - Logo
    - Design Choices
- [Features](#features)
    - Existing Features
        - Non-Logged in User
        - Logged in User
        - Staff User
    - Future Features
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
    - Cloning The Repository
    - Deploying on GitHub Pages
    - The ElephantSQL Database
- [Credits](#credits)
    - Content
    - Images
    - Education
- [Acknowledgements](#acknowledgements)

# Key Project Goals

The main goal of the site is to offer a one-stop-shop for clients of KMC Projects. This main goal can be split into smaller goals, they include
- Being able to be able to contact KMC Projects and enquire about working with them.
- See what kind of services KMC Projects offer
- Read about case studies
- Purchase parts from the distribution products list
- Login and see their purchase histroy 

# Business Model

The business model is both a business-to-customer and business-to-business as they work both with individual professionsals, companies and clients.

For business to customer, the site provides a list of products to purchase, the customer can do this without being a client of KMC Projects and can purchase as a one off item.

For business to business, the site provides business a contact form to get in touch with KMC project in order to work with them. Businesses can also purchase from the prodcuts page.

Both businesses and customers can create a login in order to see their purchase histroy. 


# Agile Development

User stories were labelled using the MoSCoW method.

[Back to Top](#kmc-projects)

# User Stories

The user stories are as follows:

## Epic

### Story

- As an XXXXX, I can XXXX so that XXXX
    - AC1 - 
    - AC2 - 
    - AC 3 - 

Tasks 
- 
-

## Epic

### Story

- As an XXXXX, I can XXXX so that XXXX
    - AC1 - 
    - AC2 - 
    - AC 3 - 

Tasks 
- 
-

## Epic

### Story

- As an XXXXX, I can XXXX so that XXXX
    - AC1 - 
    - AC2 - 
    - AC 3 - 

Tasks 
- 
-

## Epic

### Story

- As an XXXXX, I can XXXX so that XXXX
    - AC1 - 
    - AC2 - 
    - AC 3 - 

Tasks 
- 
-

## Epic

### Story

- As an XXXXX, I can XXXX so that XXXX
    - AC1 - 
    - AC2 - 
    - AC 3 - 

Tasks 
- 
-

## Epic

### Story

- As an XXXXX, I can XXXX so that XXXX
    - AC1 - 
    - AC2 - 
    - AC 3 - 

Tasks 
- 
-

## Future Stories


# User Experience

## Wireframes

Wireframes were created for each different page type, Home, Services, Products and Forms.
The Products wireframe was used as a base to create the cart & checkout pages.
The forms wireframe was used as a base to create the login, logout, sign up, contact us and newsletter pages.
This was done to keep consistancy across the site. 

Wireframe can be down in these drop downs:
<details>
<summary> Wireframe Home</summary>

![Wireframe Image Home](media/README-images/wireframe-home.png "home wireframe")

</details>

<details>
<summary> Wireframe Services</summary>

![Wireframe Image Services](media/README-images/wireframe-services.png "services wireframe")

</details>

<details>
<summary> Wireframe Items</summary>

![Wireframe Image Products](media/README-images/wireframe-products.png "products wireframe")

</details>

<details>
<summary> Wireframe Forms</summary>

![Wireframe Image](media/README-images/wireframe-forms.png "forms wireframe")

</details>


## Database Schema

The data schema was created using [drawSQL](https://drawsql.app/ "drawsql website homepage") before the project was started to get the flow and function of the models.

There are 4 custom models in this project
- The Services Model
- The CaseStudy Model
- The Contact Model
- The Boutique Ado Walkthrough Model

There are also  models that have been amended from the Boutique Ado Walkthrough to fit the requirements of the site
- The Item Model (based on the Products model)
- The Order Model (based on the Order model)
- The OrderLineItem Model (based on the OrderLineItem model)
- The UserDetials (based on the UserProfile model)

![Data Schema Image](media/README-images/custom-models.png "custom models")


## Typography

Proxima Nova was chosen from Adobe Fonts for its clean and elegant design. It is characterized by its rounded strokes and subtle variations in stroke width, giving it a warm and friendly appearance. As the client wanted a clean, minimal and industral look, proxima nova seemed like a perfect fit. 
It suits well with the logo that was already created for the business.  


## Colour Palette

![Color palette Image](media/README-images/colour-pallete.png "colour pallette image")

KMCs hero colour is #f99411, this was taken from their logo which was designed in by [JayKay Art](https://www.jay-kay.co/ "link to jaykay art homepage")

The colour pallet was craeted using the logo and the clients instructions to keep the site minimual and clean.
Different shades of grey were chosen to make the orange stand out and provide a nice contrast while keeping the look industral. 

The colour pallette also allows images added to the site to stand out.

### Logo

![Logo Image](media/README-images/logo-readme.png "image of logo")

The logo was designed in by [JayKay Art](https://www.jay-kay.co/ "link to jaykay art homepage") and was already a part of the KMC Project business. It was the only design assets the client provided and much of the sites looks and feel came from inspriation of the logo. 

Under the logo the tagline 'Hydraulic Design, Consultancy, Project Management & Training' clearly states the key services of the business and the two are often found together.

The favicon is taken from the logo itself.

![Favicon Image](media/README-images/favicon-readme.png "image of favicon")

## Design Choices

![Swim Card]( " ")

[Back to Top](#kmc-projects)

# Features

## Existing Features

## Non-Logged in User

### The Landing page

![Homepage]( " ")

### Services


### Case History and Reviews


### Products


### Login

![login]( " ")

If the username and password are not correct this error will show.

![username error]( " ")

### Register

![register]( " ")

It offers them space for a username, password and then rechecks the password to ensure it matches and there were no errors.
An example of some of the errors:

![register form errors]( " ")

The text at the bottom lets users know who already have an account that they can sign in using the login page.

### Cart

## Logged in User

### Order History

![order history]( "")

### Account Information

![]( " ")


![]( " ")


### Logout

![logout]( " logout image ")

The logout page checks if the user does wish to sign out of the site.

## Staff User

### Add Items

![]( " add items form image ")

## Edit and Delete buttons

![edit and delete buttons]( " edit and delete button image ")

## Delete Items

![delete warning]( " delete item image ")

## Future Features

[Back to Top](#kmc-projects)

# Technologies Used

- [Lucidchart](https://www.lucidchart.com/ "link to Lucidchart homepage")
Lucidchart was used to create the wireframe in the planning stages of the project
- [drawSQL](https://drawsql.app/ "Drawsql homepage")
Drawsql was used to create the data schema
- [HTML5](https://en.wikipedia.org/wiki/HTML5 "link to html5 wikipedia")
Used to create structure and content for the site.
- [CSS](https://www.w3.org/Style/CSS/Overview.en.html "link to w3")
Used to add custom styles to the site.
- [Django](https://www.djangoproject.com/ "link to django docs homepage")
The python framework used to develop the site.
- [Bootstrap](https://getbootstrap.com/ "link to bootstrap homepage")
The CSS framework used to add styles and structure to the site.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language) "link to Python wikipedia")
Used to provide functionality to the site.
- [Cloudinary](https://cloudinary.com/ "link to cloudinary homepage")
Used to host images for the site
- [ElephantSQL](https://www.elephantsql.com/ "link to elephantsql homepage")
Used to host the database used for the site.
- [Am I Responsive?](https://ui.dev/amiresponsive "Link to Am I responsive webpage")
Am I Responsive was used to see the responsive design and create screenshots of the final page on different devices.
- [Gitpod](https://www.gitpod.io/#get-started "Link to gitpod webpage")
Used to continue to create code and file structure for the respository.
- [GitHub](https://github.com/ "Link to github webpage")
GitHub was used to store the code files, README files and asset files after pushing
- [Heroku](https://id.heroku.com/login "Link to Heroku login")
Heroku was used to deploy the project. 

# Testing

Testing detail can be found [here](TESTING.md)

# Deployment

This project was developed [GitPod](https://www.gitpod.io/ "link to gitpod homepage") 

## Cloning The Repository

To clone the repository using GitHub the following steps were taken:

1. In the repository, select the "code" tab.
2. Select "HTTPS" in the dropdown menu.
3. Click the 'copy URL to dashboard button.
4. Open your chosen IDE
5. Create a new workspace and paste in the copied URL
6. Press enter

## Deploying on GitHub Pages

To deploy this page to Heroku from its GitPod repository, the following steps were taken:

1. Get Python Essentials Template from Code Institute [P3 Template](https://github.com/Code-Institute-Org/p3-template "p3 template link")
2. Create a new repository using the P3 template
3. Copy the repo URL and copy it into GitPod to create a new workspace
4. Install Django - add to requirements file
5. Create Procfile and add guricorn
6. Log in to Heroku
7. Click 'New' - 'Create new app'
8. Enter a name for the application and select the region
9. Click 'Create App'
10. Go to Settings and connect to GitHub - choose the correct repository
11. Click 'Reveal config vars' and add DISABLE_COLLECTSTATIC as the key with a value of 1
12. Go to Deploy and scroll down, click on 'Deploy Branch' to manually deploy
13. Once the app has deployed, click 'Open App' at the top of the page

## The ElephantSQL Database
ElephantSQL PostgreSQL Database was used for this project, to set up a database the following steps were taken:

1. Sign up or log in to ElephantSQL with your GitHub account.
2. Click on "Create New Instance".
3. Enter a name for the instance
4. Select "Tiny Turtle (Free)" free plan.
5. Click "Select Region".
6. Select a data centre near you.
7. Click "Review".
8. Ensure that all details are correct and then click "Create instance".
9. Copy the database URL
10. Add the database into the setting.py file

You will also need to add the database to your Django settings.py file:

DATABASES = {

'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))

}

[Back to Top](#kmc-projects)

# Credits

## Content

Wording for the site was all created by Sarah Goodwin conjunction with Kevin McCaffrey, the owner of KMC Projects

### Images


## Education

Additional learning:

- Flex calc: 
https://developer.mozilla.org/en-US/docs/Web/CSS/flex
https://aidankmcbride.medium.com/css-tips-and-tricks-81d3c641428

- json:
https://codebeautify.org/blog/how-to-create-json-file/

- text editor:
https://www.youtube.com/watch?v=mF5jzSXb1dc

- choice fields
https://docs.djangoproject.com/en/5.0/ref/models/fields/
https://www.geeksforgeeks.org/how-to-align-checkboxes-and-their-labels-on-cross-browsers-using-css/

# Acknowledgements

- Mentor, Lauren-Nicole, for all her help and support, the useful resources she provided and for being a friendly face throughout! Could not have done this project without her!!
- Friends and family who helped test the site on different devices and give real world user feedback


[Back to Top](#kmc-projects)

