# Paul Reed

Paul Reed is an online luxury homeware store selling a range of furniture, utensils, and decorative objects. The site allows users to purchase products as a registered user or a guest.

The site uses HTML5, CSS3, JavaScript, Python, Django, and ElephantSQL.

[View the live site here](https://cimsp4v1.herokuapp.com/ "Paul Reed")

## Contents

1. [Project Objectives](#1-project-objectives)
2. [User Experience](#2-user-experience)
3. [Features](#3-features)
4. [Technologies Used](#4-technologies-used)
5. [Testing](#5-testing)
6. [Deployment](#6-deployment)
7. [Credits](#7-credits)

## **1. Project objectives

**As a user, I want to...**

  1. Understand the site's main purpose and find out more about what the site offers
  2. Navigate within the site to find relevant content
  3. View items without having to create an account
  4. View and sort items by category and price
  5. Purchase items without having to create an account
  6. Update and remove items from my bag
  7. Register for an account if I choose to
  8. Find the site's contact details, including social media links, and be able to contact the site
  9. Log in to my account (returning user)
  10. Share reviews of items I have purchased (returning user)
  11. View my previous orders (returning user)

**As a superuser, I want to...**

  1. Log in to my account
  2. Add, edit, and delete items
  3. Delete user reviews

## **2. User experience**

**Colour scheme**

The color scheme is based on shades of blue and grey.

> ![colour-palette](/ci_msp4/docs/colour-palette.webp)

**Typography**

The brand font is Inspiration with a cursive fallback font.

> ![brand-font](/ci_msp4/docs/brand-font.webp)

The primary font is Roboto with a sans-serif fallback font.

> ![primary-font](/ci_msp4/docs/primary-font.webp)

**Imagery**

All images are representative of the items in the products section.

**Interactive links**

The site includes internal hyperlinks to the different pages of the site and external hyperlinks to Facebook, Twitter and Instagram, which open in a new browser tab.

The contact page includes an email address hyperlink that will automatically open a user's email application and autofill the email address in the "To" field, the subject 'Mail from our site' in the "Subject" field, and the text 'Thank you for contacting us. Please let us know how we can help you...' in the body.

**Wireframes**

Wireframes for desktop and mobile views were created using [Balsamiq](https://balsamiq.com/wireframes/ "Balsamiq").

[View the desktop and mobile wireframes here](docs/wireframes/ "Wireframes")

Wireframes were created for desktop and mobile views only. It was considered that this would be sufficient to inform the layout of the tablet view.

Similarly, wireframes were created for the homepage, recipes page, and full recipe page only. It was considered that this would be sufficient to inform the design of other pages.

**Database scheme**

The site uses a relationship database. ElephantSQL manages the SQL data for the various applications.

> ![db-scheme](/ci_msp4/docs/db-scheme.webp)

## **3. Features**

The site is designed to be responsive on all devices.

## **4. Technologies used**

**Languages used**

- [HTML5](https://en.wikipedia.org/wiki/HTML5 "HTML5")

- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets "CSS3")

- [JavaScript](https://en.wikipedia.org/wiki/JavaScript "JavaScript")

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language) "Python")

**Frameworks, Libraries and Programes Used**

- [Heroku](https://devcenter.heroku.com/) is where the live site is deployed.

- [Bootstrap v5](https://getbootstrap.com/docs/5.0/getting-started/introduction/ "Bootstrap v5") was used to assist with the responsiveness and styling of the website.

- [ElephantSQL](https://www.elephantsql.com//) was the relational database used to host the database.

- [pip](https://pip.pypa.io/en/stable/) is the package installer for Python, allowing us to install the packages we need for this site.

- [Google Fonts](https://fonts.google.com/ "Google Fonts") was used to import the Bubblegum Sans and Nunito fonts into the style.css file, which are used throughout the website.

- [Font Awesome](https://fontawesome.com/ "Font Awesome") was used to add icons for aesthetic and UX purposes throughout the website.

- [Hover.css](https://ianlunn.github.io/Hover/ "Hover.css") was used on the links in the navbar to add the underline-from-center transition on hover.

- [jQuery](https://jquery.com/ "jQuery") is included in Boostrap to make the navbar responsive.

- [Git](https://git-scm.com/ "Git") was used for version control by using the Gitpod terminal to commit to Git and push to GitHub.

- [GitHub](https://github.com/ "GitHub") was used to store the project code after being pushed from Git.

- [Balsamiq](https://balsamiq.com/ "Balsamiq") was used to create the wireframes during the design process.

## 5. Testing

**W3C markup validator**

The [W3C Markup Validator](https://validator.w3.org/ "W3C Markup Validator") was used to to validate the site's HTML.

Copies of the reports for each page can be accessed [here](/ci_msp4/docs/tests/html_validator/ "W3C Markup Validator report").

**W3C CSS validator**

The [W3C CSS Validator](https://jigsaw.w3.org/css-validator/ "W3C CSS Validator") was used to validate the site's CSS. Warnings related to Bootstrap CSS, vendor extensions, vendor extended pseudo-elements, and vendor extended pseudo-classes were ignored.

Copies of the reports for each page can be accessed [here](/ci_msp4/docs/tests/css_validator/ "W3C CSS Validator reports").

**Lighthouse testing**

The website was tested using Lighthouse on the Chrome and Microsoft Edge browsers to determine the website’s performance, accessibility, best practices, and SEO.

For desktop and mobile, on both Chrome and Edge, accessibility, best practice, and SEO scored at least 90%.

For desktop and mobile, on both Chrome and Edge, performance scored less than 90% (with the exception of Edge mobile, which scored at least 90%). This was considered acceptable at this time; however, the developer may look to improve this in the future.

The reports can be viewed below:

- [Chrome Desktop](/ci_msp4/docs/tests/chrome-lighthouse-desktop-1.pdf "Chrome Desktop report")

- [Chrome Mobile](/ci_msp4/docs/tests/chrome-lighthouse-mobile-1.pdf "Chrome Mobile report")

- [Edge Desktop](/ci_msp4/docs/tests/edge-lighthouse-desktop-1.pdf "Edge Desktop report")

- [Edge Mobile](/ci_msp4/docs/tests/edge-lighthouse-mobile-1.pdf "Edge Mobile report")

**a11y color contrast accessibility validator**

The [ally Color Contrast Accessibility Validator](https://color.a11y.com/Contrast/ "ally Color Contrast Accessibility Validator") was used to test for color contrast problems. The Validator retuend 1 problem with contrast color-pairs. This problem was resolved by adjusting the contrast of the font color.

A copy of the original report can be accessed [here](/ci_msp4/docs/tests/a11y-contrast-accessibility-validator-1.pdf "ally Color Contrast Accessibility Validator report").

A copy of the final report can be accessed [here](/ci_msp4/docs/tests/a11y-contrast-accessibility-validator-2.pdf "ally Color Contrast Accessibility Validator report").

**Responsiveness testing**

The website's responsiveness was tested manually, using the Google Chrome DevTools, and the [Responsive Design Cheker](https://responsivedesignchecker.com/ "Responsive Design Checker") website.

The website was responsive on all screen sizes from 320x480px to 1920x1200px.

**Jest Automated Testing**

Automated tests were performed using the Jest testing framework.

No issues were experienced.

**Testing project objectives**

Click on links to view supporting images.

***User objectives***

| Feature | Expected result | Actual result |
| ----------- | ----------- | ----------- |
| Understand the site's main purpose and find out more about what the site offers | Clear and relevant text and imagery on the landing page to let users know what the site offers  | As expected |
| Navigate within the site to find relevant content | Easy to use navigation bar at the top of the page; Quick links in the page footer; clear buttons and links throughout the site | As expected<br> [Navbar](/ci_msp4/docs/navbar.webp "Navbar")<br> [Footer](/ci_msp4/docs/footer.webp "Footer")   |
| View items without having to create an account | View all items by category from the navigation bar and open individual items to view details | As expected<br> [Category](/ci_msp4/docs/category.webp "Category") |
| View and sort items by category and price | Sort items by category (A-Z and Z-A) and by price (low-high and high-low) using a simple dropdown box | As expected<br> [Sort](/ci_msp4/docs/sort.webp "Sort") |
| Purchase items without having to create an account | Add items to bag and checkout as a guest | As expected |
| Update and remove items from my bag | Change the quantity of items in the bag and remove items as needed |  |
| Register for an account if I choose to | Register for an account and receive confirmation that an account has been created | As expected<br> [Signup](/ci_msp4/docs/signup.webp "signup") |
| Find the site's contact details, including social media links, and be able to contact the site | Link to contact page with details and contact form with confirmation that message has been sent | As expected |
| Log in to my account (returning user) | Log in to account and be directed to profile page | As expected<br> [Log in](/ci_msp4/docs/sign-in.webp "Log in") |
| Share reviews of items I have purchased (returning user) | Create reviews for items when logged in to account | As expected<br> [Add review](/ci_msp4/docs/add-review.webp "Add review") |
| View my previous orders (returning user) | View list of items purchased previously when logged in to account | As expected |

***Superuser objectives***

| Feature | Expected result | Actual result |
| ----------- | ----------- | ----------- |
| Log in to my account | Log in to account and be directed to profile page | As expected<br> [Log in](/ci_msp4/docs/sign-in.webp "Log in") |
| Add, edit, and delete items | Add new items, edit existing items, and delete items | As expected<br>[Add item](/ci_msp4/docs/add-product.webp "Add item")<br> [Edit product](/ci_msp4/docs/edit-product.webp "Edit item")<br> [Delete item](/ci_msp4/docs/delete-product.webp "Delete product")<br> [Confirm delete](/ci_msp4/docs/confirm-delete.webp "Confirm delete") |
| Delete user reviews | Delete user reviews as needed | As expected |

**Known Bugs**

- The email subscription form on the footer has no functionality at present
- The sort by price filter does not account for sale price

## 6. Deployment

**Deployment to Heroku**

 Heroku was used to deploy this project. The steps used for deployment to Heroku are as follows:

  1. Sign up and log into heroku.
  2. On the top right hand corner of the heroku website, click new, then create new app.
  3. Name the app, select region, and then click the create app button.
  4. Install postgres under the resources tab.
  5. Insert relevant config vars into heroku, such as IP, PORT SECRET_KEY, DATABAS_URL.
  6. You can click connect to github but this project used the CLI method.
  7. Log into heroku via CLI.
  8. Create a git remote for heroku.
  9. Push all changes to the staging area.
  10. Push to heroku for your app to run and function.

## 7. Credits

**Code**

- [Bootstrap v5](https://getbootstrap.com/docs/5.0/getting-started/introduction/ "Bootstrap v5") was used to assist with the responsiveness and styling of the website.

**Information Sources/Resources**

The following sources were used to provide additional information relating to HTML, CSS, and Django:

- [W3C Schools](https://www.w3schools.com/ "W3C Schools") 

- [Stack Overflow](https://stackoverflow.com// "Stack Overflow") 

- [Django](https://docs.djangoproject.com/en/4.1/ "Django Documentation")

**Content**

All content was written or adapted by the developer with the exception of the product descriptions, images, and policy text, which were sourced from Stone the Crows (https://www.stonethecrowsretail.co.uk/).

**Media**

All images were used under Creative Commons where available, or under the provisions for research and private study in section 29 of the Copyright, Designs and Patents Act 1988.

All images were converted to .webp (where necessary) using [online-convert](https://www.online-convert.com/ "online-convert").

**Acknowledgements**

Thank you to my mentor, Dario Carrasquel for his helpful feedback, the web developer community on Twitter, and to tutor support at Code Institute for their support and patience.