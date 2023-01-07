# Paul Reed

Paul Reed is an online luxury homeware store selling a range of furniture, utensils, and decorative objects. The site allows users to purchase products as a registered user or a guest.

The site uses HTML5, CSS3, JavaScript, Python, Django, and ElephantSQL.

[View the live site here](https://mattgriffindev.github.io/hi-lo/ "Paul Reed")

## **1. User experience**

### User stories

**As a user, I want to...**

  1. Understand the site's main purpose and find out more about what the site offers
  2. Navigate within the site to find relevant content
  3. View items without having to create an account
  4. View and sort items by category and price
  5. Purchase items without having to create an account
  6. Register for an account if I choose to
  7. Find the site's contact details, including social media links, and be able to contact the site
  8. Log in to my account (returning user)
  9. Share reviews of items I have purchased (returning user)
  10. View my previous orders (returning user)

**As a superuser, I want to...**

  1. Log in to my account
  2. Add, edit, and delete items
  3. Delete user reviews

**How this is achieved**

**Design**

 - The site uses a simple and consistent layout and design.

**Navigation**

 - Users can access different categories and sub-categories of itmes from the navbar.

![navbar](/ci_msp4/docs/navbar.webp)

 - User can access categories by hovering over the hero images.

![hero-image](/ci_msp4/docs/hero-image.webp)

**Items**

 - Users can add a review for individual items.

 ![add-review](/ci_msp4/docs/add-review.webp)

 - Users can access recipes without having to register or login.
 - Registered users can share their own recipes.
 - Registered users can view their own recipes on their profile page.

  ![profile recipes](cakebox/static/img/profile-recipes.png)

**Register, Login, and Logout**

 - Users can login or register using the buttons in the navbar. 

![login-register](/ci_msp4/docs/login-register.webp)

 - Users can register for an account easily.

![signup](/ci_msp4/docs/signup.webp)
 
 - Users can login to their account easily.

![sign-in](/ci_msp4/docs/sign-in.webp)

 - Users can logout of their account from the navbar.

![logout](/ci_msp4/docs/logout.webp)

**Defensive programming**
   
Some actions can only be performed by superusers.

- Superusers can add items.

![add-product](/ci_msp4/docs/add-product.webp)

- Superusers can edit items.

![edit-product](/ci_msp4/docs/edit-product.webp)

- Superusers can delete items.

![delete-product](/ci_msp4/docs/delete-product.webp)

- Superusers will get an alert asking them if they are sure they want to delete the item.

![delete-alert](/ci_msp4/docs/delete-product.webp)

**Colour scheme**

The color scheme is based on shades of blue and grey.

![colour-palette](/ci_msp4/docs/colour-palette.webp)

**Typography**

The brand font is Inspiration with a cursive fallback font.

![brand-font](/ci_msp4/docs/brand-font.webp)

The primary font is Roboto with a sans-serif fallback font.

![primary-font](/ci_msp4/docs/primary-font.webp)

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

ElephantSQL manages the data for the various applications

![db-scheme](/ci_msp4/docs/db-scheme.pdf)

## **2. Features**

The site is designed to be responsive on all devices.

## **3. Technologies userd**

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

## 4. Testing

**W3C markup validator**

The [W3C Markup Validator](https://validator.w3.org/ "W3C Markup Validator") was used to to validate the site's HTML. The Validator returned 4 warnings and 1 error.

A copy of the original report can be accessed [here](docs/tests/html-validator-1.pdf "W3C Markup Validator report").

A copy of the final report can be accessed [here](docs/tests/html-validator-2.pdf "W3C Markup Validator report").

**W3C CSS validator**

The [W3C CSS Validator](https://jigsaw.w3.org/css-validator/ "W3C CSS Validator") was used to validate the site's CSS. The Validator returned no warnings.

A copy of the report can be accessed [here](docs/tests/css-validator-1.pdf "W3C CSS Validator report").

**Lighthouse testing**

The website was tested using Lighthouse on the Chrome and Microsoft Edge browsers to determine the website’s performance, accessibility, best practices, and SEO.

For desktop, all measures scored at least 90% 

For mobile, the performance measure scored 83% and 87% on Chrome and Edge respectively. This was considered acceptable at this time; however, the developer may look to improve this in the future.

The reports can be viewed below:

- [Chrome Desktop](docs/tests/lighthouse-chrome-desktop.pdf "Chrome Desktop report")

- [Chrome Mobile](docs/tests/lighthouse-chrome-mobile.pdf "Chrome Mobile report")

- [Edge Desktop](docs/tests/lighthouse-edge-desktop.pdf "Edge Desktop report")

- [Edge Mobile](docs/tests/lighthouse-edge-mobile.pdf "Edge Mobile report")

**a11y color contrast accessibility validator**

The [ally Color Contrast Accessibility Validator](https://color.a11y.com/Contrast/ "ally Color Contrast Accessibility Validator") was used to test for color contrast problems. The Validator retuend 1 problems with contrast color-pairs. These problems were resolved by adjusting the contrast of the font color.

A copy of the original report can be accessed [here](docs/tests/a11y-contrast-checker-1.pdf "ally Color Contrast Accessibility Validator report").

A copy of the final report can be accessed [here](docs/tests/a11y-contrast-checker-2.pdf "ally Color Contrast Accessibility Validator report").

**Responsiveness testing**

The website's responsiveness was tested manually, using the Google Chrome DevTools, and the [Responsive Design Cheker](https://responsivedesignchecker.com/ "Responsive Design Checker") website.

The website was responsive on all screen sizes from 320x480px to 1920x1200px.

**Known Bugs**

No bugs have been identified.

## 5. Deployment

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

## 6. Credits

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