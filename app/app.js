'use strict';

var images = [{
    "src":"https://scontent.fmnl4-4.fna.fbcdn.net/v/t1.0-0/p110x80/13177650_1128825090472233_6694309210504674839_n.jpg?oh=a86642d8a14f1d983db909e492eb6c9d&oe=57C735E7",
    "caption": "Maeve and Jolibee"
  },
    {
      "src":"https://scontent.fmnl4-4.fna.fbcdn.net/v/t1.0-9/10341415_1098047106883365_1884754102383937542_n.jpg?oh=d5dde597344d804df650f2396306ae8d&oe=57DA4837",
      "caption": "Happy birthday Maeve"
    },
    {
      "src":"https://scontent.fmnl4-4.fna.fbcdn.net/v/t1.0-0/p206x206/11202111_958810744140336_416534854045418989_n.jpg?oh=9d2a4b5b1712eb516ec8a7bd0898b011&oe=57C71278",
      "caption":"Sisay and Maeve"
    },
    {
       "src": "https://css-tricks.com/wp-content/uploads/2013/06/photo-wedding_1200x800.jpg",
        "caption":"Wedding Celebration"
    },
     {
       "src": "http://img1.ak.crunchyroll.com/i/spire1/2df2ab0df7bd63d0b8b257b4bb1231641383245215_fwide.jpg",
       "caption":"One Piece"
     },
     {
       "src": "https://lh3.googleusercontent.com/3kPZdXkkA7nhrD6c6AXPUqB5ZV1i-qs-ACmWJoUWfzgGzoYobFj2xeGU-JKxC_Tz_NIIsJ1fjg=s640-h400-e365",
       "caption":"One Punch Man"
     }
   ];
angular.module('myApp', [])
.controller('myController', function() {
this.showCaption = true;
this.header = "Image Gallery";
this.images = images;
this.current = 0;
this.addImage = function() {
    var image = {"src":this.imageSrc};
    this.images.push(image);
    this.imageSrc ="";
}

this.getIndex = function(img) {
  this.current = this.images.indexOf(img);

}
 this.nextImage = function() {
   this.current += 1;
   if (this.current===this.images.length)
     this.current = 0;
 }
});
