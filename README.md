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
    - [Target Audience](#target-audience)
- [Agile Development](#agile-development)
- [User Stories](#user-stories)
    - [Future Stories](#future-stories)
- [Web Marketing](#web-marketing)
    - [SEO Implementation](#seo-implementation)
- [User Experience](#user-experience)
    - [Wireframes](#wireframes)
    - [Database Schema](#database-schema)
    - [Typography](#typographt)
    - [Colour Palette](#colour-palette)
    - [Logo](#logo)
- [Features](#features)
    - [Existing Features](#existing-features)
    - [Future Features](#future-features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
    - [Cloning The Repository](#cloning-the-repository)
    - [Deploying on GitHub Pages](#deploying-on-github-pages)
    - [The SQL Database]()
- [Credits](#credits)
    - [Content](#credits)
    - [Images](#images)
    - [Education](#education)
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

## Target Audience

KMC Projects target audience focus on the hydraulic industry, businesses involved in construction, manufacturing, infrastructure development, and related sectors. Their clients often know what they need before coming to the site.
The audience main goals are to
- Contact KMC Project
- Find parts they are already looking for

# Agile Development

User stories were labelled using the MoSCoW method.

[Back to Top](#kmc-projects)

# User Stories

The user stories are as follows:

## User Stories

### Generic User (Guest):
- As a guest user, I can browse through the services offered by KMC Projects so that I can understand the scope of the company's expertise.
- As a guest user, I can view case studies on past projects completed by KMC Projects so that I can assess the quality of their work.
- As a guest user, I can access the site's product list to explore the range of products offered by KMC Projects.
- As a guest user, I can access the site's content to learn about the company's mission, values, and team member.
- As a guest user, I can sign up to the newsletter to keep up to date with the company's latest news and updates.
- As a guest user, I can use the contact form to get in touch with KMC Projects.

### Registered (Logged in) User:
- As a logged-in user, I can create and manage my account profile on KMC Projects so that I can personalize my experience on the site.
- As a logged-in user, I can view my order history from past orders
- As a logged-in user, I can update my delivery information to save for future orders

### Admin User:
- As an admin user, I can add new services to the offerings provided by KMC Projects
- As an admin user, I can create and update case studies showcasing successful projects completed by KMC Projects.

### Shopper:
- As a shopper, I can search for specific products or services offered by KMC Projects to find what I need efficiently.
- As a shopper, I can add items to my cart and proceed to checkout seamlessly on KMC Projects.
- As a shopper, I can save my delivery information 
- As a shopper, I can add item to my cart so that I can review them before purchase

## Future Stories

### Registered (Logged in) User:
- As a future registered user, I would be able to see my contact form responses and make amends to them

### Admin User:
- As a future admin user, I would be able to view a list of the contact forms that site users had filled out without going to the django admin panel
- As a future admin user, I would be able to view a list of the newsletter signsups without going to the django admin panel
- As a future admin user, I would be able to edit the products list page without going to the django admin panel

### Shopper:
- As a future shopper, I would be able to request certain parts be made avalaible 
- As a future shopper, I would be notified if a new product was made avalaible 

# Web Marketing

For this project the following web marketing strategies were used:

- SEO and content marketing
- Social media marketing
- Email newsletter subscription

## SEO Implementation

To implement SEO in this project, various techniques were used. These include using semantic HTML, avoiding excessive keyword repetition, integrating keywords naturally within website content, providing descriptive alt attributes for images, incorporating metadata descriptions and keywords at the head level of the project, and using the 'noopener' attribute in the 'rel' tag. Additionally, we ensure that external links have descriptive 'aria-label' attributes for enhanced accessibility.

The keywords are short-tailed and long-tailed and are as follows:

Short-tailed Keywords:
 - Hydraulic Design
 - Consultancy
 - Project Management
 - Training
 - Problem-solving
 - Fluid power
 - Engineering
 - Hydraulic Solutions

Long-tailed Keywords:
- Hydraulic Design Excellence
- Hydraulic Consultancy Services
- Project Management for Hydraulic Systems
- Hydraulic Training Programs
- Innovative Hydraulic Solutions
- Precision Hydraulic Engineering
- Efficient Hydraulic Systems
- Expert Hydraulic Engineers
- Hydraulic Product Distribution List
- Quality Hydraulic Products for Purchase

A robots.txt file is included at the project's root level. This file instructs search engine crawlers about the URLs they can access on the website. Its primary purpose is to prevent the site from being overwhelmed by excessive requests. It's important to note that robots.txt isn't intended to exclude web pages from Google; rather, it serves as a tool for managing crawler access.

The project's root level also includes a sitemap.xml file. This file serves as a catalog of a website's crucial pages, ensuring that Google can locate and index them effectively. It aids search engines in comprehending the structure of your website. It's crucial for Google to index all significant pages of your website. However, certain pages may lack internal links, making them challenging for search engines to discover. A sitemap can expedite the process of content discovery in such cases.

## Social Media Marketing

Facebook was used as the primary social media platform for web marketing due to its extensive user base and broad demographic reach. The objective of establishing a Facebook business page is to attract the attention of potential customers and to showcase the company's products and services effectively. A real business facebook account was created and at the time of submission was active it can be found here [KMC Projects Facebook](https://www.facebook.com/profile.php?id=61558802589438 "KMC Project Facebook page")

![KMC Project Facebook](media/README-images/facebook-img.png "KMC Project Facebook page")

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
Some of the fields in the below images do not reflect the final data types used – please see the app for the true data types.

There are 4 custom models in this project
- The Services Model (full CRUD)
- The CaseStudy Model (full CRUD)
- The Contact Model
- The NewsLetterSignUp Model

![Data Schema Image](media/README-images/custom-models.png "custom models")

There are also  models that have been amended from the Boutique Ado Walkthrough to fit the requirements of the site
- The Item Model (based on the Products model)
- The Order Model (based on the Order model)
- The OrderLineItem Model (based on the OrderLineItem model)
- The UserDetials (based on the UserProfile model)

A full data schema was used using `django-extensions` > `pydot` > `python manage.py graph_models -a > all_models.dot` visualising the dot file with [GraphvizOnline](https://dreampuf.github.io/GraphvizOnline/ "GraphvizOnline website")

![All Data Schema Image](media/README-images/models.png "all models")

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

[Back to Top](#kmc-projects)

# Features

## Existing Features

### Home

![Homepage](media/README-images/home.png "home screenshot")

The homepage clearly shows the logo, the tag line, the company values and gives easy access to the nav bar. 
It provides access to one of the sites main functions for contacting KMC Projects and gives the user knowledge they have landed in the right place by showing 'Problems Solved', one of KMC mottos. 

The homepage shows a bright image of hydraulic cyclinders giving users another visual sense of the site.
The homepage is responsive on all screen sizes.

#### About

![About](media/README-images/about.png "about screenshot ")

Also on the homepage there is an about section, giving some more details into the director of the company, providing trust with the users. 

The about section is responsive on mobile with the image of Kevin moving above the text for better UX.

### Navbar

![Navbar](media/README-images/nav-bar.png "nav bar screenshot")

The nav bar is clean and simple, providing clear call to actions for users to access the site from. 
From the nav bar users can tell if they are logged in or not due to the changing navigation. 

![Navbar-logged in nav-bar](media/README-images/logged-in-navbar.png "logged-in navbar screenshot")

The nav bar is resposnive on mobile and reduces to a hamburger menu on smaller screen sizes.

![Navbar-hamburger](media/README-images/hamburger.png "hamburger screenshot")

The hamburger opens clearly showing the call to actions. 

![Navbar-hamburger open](media/README-images/hamburger-open.png "hamburger-open screenshot")

### Footer

![Footer](media/README-images/footer.png "footer screenshot ")

The footer has links to contact details, both the business phone number and the contact us form.

It has links to social media for KMC Project and/or Kevin McCaffrey the director.
It has a Newsletter sign up form for those who wish to be kept up to date with the business.

It has access to the site creator’s github.


### Services

![Services](media/README-images/services.png "services screenshot ")

The services page gives users an idea of some of the services to discuss with KMC Projects in the contact form. It goes through 3 of their main offerings. 
- Hydraulic Consultancy Services
- Project Management for Hydraulic Systems
- Hydraulic Training Programs

For SEO these titles were changes from Consultancy, Project Management & Training. 

The price of these services has not been included as every service is bespoke to each client and the job specs must be discussed before a quote is offered.


### Case Study

![Case Study](media/README-images/casestudy.png "case study screenshot")

The case study showcases some of the work KMC Project is involved in, giving users an idea of the type of work they could expect if they were to become a clients. 

### Products

![Products](media/README-images/products.png "products screenshot")

The products page has the option the view all products or to view by product type.
Users can search by product name or item number. When in discussions with Kevin from KMC Projects about the products page, he said his clients knew the item number they would be looking for and would not come to the site in search of a price or to browse types of an item. This is why the products page is clean and simple, just the way KMC Projects wanted it.

Users have the option to add the item to their carts, and choose how many items they wish to add. 
The products themselves list
- The name
- The price in NZD
- The item number which is unique to each item
- The manufacturer
- A datasheet pdf 

The products page is responsive and changes for mobile users

### Cart

![Homepage]( " ")

### Checkout

![Homepage]( " ")

### Login, Logout and Sign Up

![login]( " ")

If the username and password are not correct this error will show.

![username error]( " ")

### Forgot Password

![Homepage]( " ")

![Homepage]( " ")

### Register

![register]( " ")

It offers them space for a username, password and then rechecks the password to ensure it matches and there were no errors.
An example of some of the errors:

![register form errors]( " ")

The text at the bottom lets users know who already have an account that they can sign in using the login page.

### Logout

![logout]( " logout image ")

The logout page checks if the user does wish to sign out of the site.

### Admin Access

![Homepage]( " ")

### Account

![Account Page]( " ")

Users can save their delivery information on their account page and this will pull through to the orders page.
They will also be able to see their order history in a drop down list, showing the date they made the order and then the details.


### Order History

![order history]( "")

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

## The CI Database
CI Database was used for this project, to set up a database the following steps were taken:

1. Sign up or log in to ElephantSQL with your GitHub account.
2. 

You will also need to add the database to your Django settings.py file:

DATABASES = {

'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))

}

[Back to Top](#kmc-projects)

# Credits

## Content

Wording for the site was all created by Sarah Goodwin conjunction with Kevin McCaffrey, the owner of KMC Projects

### Images

Images were created in Canva, suppplied by the client or taken from google images.

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

- Superusers
https://stackoverflow.com/questions/15998140/how-to-limit-a-view-to-superuser-only 

- Send emails
https://docs.djangoproject.com/en/5.0/topics/email/
https://simpleisbetterthancomplex.com/tutorial/2016/06/13/how-to-send-email.html
https://github.com/AnaMelisaGo/portfolio-5-green-planet/tree/1f5410657463b6c116d5fb6d87a9875348d427f8/checkout/templates/checkout/confirmation_emails

# Acknowledgements

- Mentor, Lauren-Nicole, for all her help and support, the useful resources she provided and for being a friendly face throughout! Could not have done this project without her!!
- Friends and family who helped test the site on different devices and give real world user feedback


[Back to Top](#kmc-projects)

