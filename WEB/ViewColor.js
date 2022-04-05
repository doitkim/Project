var Links ={
  setLinkColor(color){
    //var alist = document.querySelectorAll('a');
    //var i = 0;
    //while(i < alist.length){
    //  alist[i].style.color = color;
    //  i = i + 1;
    //}
    $('a').css('color', color)
  }
}
var Body ={
  setBackgroundColor(color){
    //document.querySelector('body').style.backgroundColor = color;
    $('body').css('backgroundColor', color);
  },
  setFontColor(color){
    //document.querySelector('body').style.color = color;
    $('body').css('color', color);
  }
}


function NighitDayHandler(self){
if(self.value === '밤')
{
  Body.setBackgroundColor('black');
  Body.setFontColor('white');
  Links.setLinkColor('powderblue');
  self.value='낮'
}
else
  {
    Body.setBackgroundColor('white');
    Body.setFontColor('black');
    Links.setLinkColor('blue');
    self.value = '밤'
  }
}
