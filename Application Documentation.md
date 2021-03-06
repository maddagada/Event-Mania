# User Stories

 1. As a User I want to view the pictures of their previously organized events in the gallery, so I can know the work quality and type of events they organized so far.
 
 ###### Acceptance Criteria:
    
    I can see the images of the previous events

 2. As a User I want to contact them through the mobile, so I can discuss any details that I am willing to know over the phone.
 
  ###### Acceptance Criteria:
  
     I can see a mobile number
     
     I can see an email address
  
 3. As a User I want to know what all the rental party supplies they have, so I can contact them based on availability of item.
 
  ###### Acceptance Criteria:
  
     I can see the party rental supplies by product 
     
     I can see the images of the items by product
     
     I can see the price of the item per day
     
 4. As a User I want to know the number of pieces available per item and items delivery options, so I can confirm on renting an item with them
 
  ###### Acceptance Criteria:
  
     I can able to see Add to the cart option below the image 
     
     I can able to see the Get Quote option upon the RENT button click
     
 5. As a User I want to know the item quote form submission is success, so I can be sure that I will hear back from them.
 
  ###### Acceptance Criteria:
     
     I can able to see the confirmation message received to the Gmail-id given in the form. 
     
 6. As a Admin I want to add an new party item to the product page or able to update the gallery page with the image of events organized , so I can maintain website with updated work
 
  ###### Acceptance Criteria:
  
     I can able to add/update the images in the gallery
     
     I can able to add/update rental items in the product page
# MisUser Stories

1. As a wicked user, I would like to perform Denial of service attack to make the page unavailable to the legitimate user

    ###### Mitigation:

       Whitelisting/blacklisting the IP addresses
       
       Limiting the amount of traffic to a network interface controller
   
2. As a malicious user I want to execute malicious script through the browser, so I can hijack the user sessions by stealing their cookies and session tokens

    ###### Mitigation:

       By validating the user input, we can prevent the XSS attack. Input validation prevents user from adding special characters into the field.
       
       Cross-site scripting attack can be mitigated by sanitizing user input.

   
3. As a malicious hacker I would like to attack on the application using phishing techniques.

    ###### Mitigation:

       SPAM filters help in detecting the known viruses, blank senders.
       
       Updating systems frequently with the latest security versions and patches will reduce the chances of attack.


4. As a malicious attacker I want to perform malicious SQL statements against the database server, so I can get control over the database and perform CRUD operations.

    ###### Mitigation:

       Prepared statements with parametrized queries help in mitigating this attack 
   
       Applying the principle of least privilege security control help in minimizing the damage of attack.
       
# Diagrams

 ## MockUp Diagrams
 
 **Home Page Mock Up**
 
 ![Home Page](https://github.com/maddagada/Event-Mania/blob/master/Architecture%20and%20Mockup%20Images/HomePage_Mockup.PNG)
 
 **Gallery Page Mock Up**
 
 ![Gallery Page](https://github.com/maddagada/Event-Mania/blob/master/Architecture%20and%20Mockup%20Images/GalleryPage_Mockup.PNG)
 
 **Contact Us Page**
 
 ![Contact Us](https://github.com/maddagada/Event-Mania/blob/master/Architecture%20and%20Mockup%20Images/ContactUs_Mockup.PNG)
 
 **Party Rental Items Page**
 
 ![Party Rental](https://github.com/maddagada/Event-Mania/blob/master/Architecture%20and%20Mockup%20Images/PartyRentalCategory_Mockup.PNG)
 
 **Party Rental Individual Item Page**
 
 ![Individual Item Page](https://github.com/maddagada/Event-Mania/blob/master/Architecture%20and%20Mockup%20Images/PartyRental_AddtoCart.PNG)
 
 **Review Cart**
 
 ![Cart Page](https://github.com/maddagada/Event-Mania/blob/master/Architecture%20and%20Mockup%20Images/ReviewCart.PNG)
 
 **Quote Submission Page**
 
 ![Quote](https://github.com/maddagada/Event-Mania/blob/master/Architecture%20and%20Mockup%20Images/QuoteSubmissionPage.PNG)
 
 ## Architecture Diagrams
 
 **System Context Level**
 
 ![System Context](https://github.com/maddagada/Event-Mania/blob/master/Architecture%20and%20Mockup%20Images/System%20Contex%20Level%20Architecture.PNG)
 
 **Container Context Level**
 
 ![Container Context](https://github.com/maddagada/Event-Mania/blob/master/Architecture%20and%20Mockup%20Images/Container%20Level%20Artchitecture.PNG)
 
 **Component Level**
 
 ![Component](https://github.com/maddagada/Event-Mania/blob/master/Architecture%20and%20Mockup%20Images/Component%20Level%20Architecture.PNG)
