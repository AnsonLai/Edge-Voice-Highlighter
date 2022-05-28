# Edge Voice Highlight Injector (PROOF OF CONCEPT)

Microsoft Edge browser has the BEST read aloud feature.  It will read out any webpage with natural sounding voices.  This highlighter allows you to use voice commands ("note!") to highlight what is being currently read.  If you go out for a jog and listen to a webpage, you can come back and see all the important sections you've highlighted.

## Demo

1. Go to: <https://ansonlai.github.io/Edge-Voice-Highlighter/>
2. Pick a random webpage and inject the code (might take 3 or 4 seconds)
3. Allow microphone recording
4. Use Microsoft Edge's built in **Read Aloud** feature
5. Say "note!" to highlight the current text
6. When you're done:
    1. Scroll to the top and click "Show Highlights" button to extract all highlights **OR**
    2. Screenshot the page for future reference

### Options

* **Noise Threshold**
  * Determines how loud you have to say the keyphrase
* **Lookback Distance**
  * When you extract all highlights, determines how much of the surrounding text to capture
* **Show Highlights**
  * Click to see extracts of all your highlighted text at the top of the page

## Tips

* Select a good voice for Read Aloud in Voice Options.  I like *Microsoft Sonia Online Natural* for English.
* If you are on mobile and want to keep listening even if your screen is off, turn on "Read aloud background play"
  * Go to "<edge://flags/>" on the browser, and find "Read aloud background play", make sure it is enabled
* If you want to save your highlights, screenshot the page
  * On Desktop, do a Web Capture with Ctrl+Shift+S
  * On Mobile, click the share icon, and choose the built-in scrolling screenshot feature
* There's really no keyphrase, any shout or noise will highlight the text
* If you have your own books or documents, you will want to host them somewhere
  * Convert them to html first at sites like
    * (EPUB) <https://convertio.co/epub-html/>
    * (PDF) <https://convertio.co/pdf-html/>
  * Then host them online at <https://tiiny.host/web-hosting-free-sites/>

## Contribute

This is a buggy proof of concept, and I'm happy to accept contributions!  If there's enough interest, I will try and polish this.  At the moment, it works for my personal use.

### Limitations

Any developer will be asking why I'm using such a convoluted process.  In short, Microsoft Edge on Android doesn't have extensions or a developer console.  This API and webpage is the only way I can inject the code onto a random webpage on my phone.  It destroys the styling and some images, but the text comes through just fine.

### Building Blocks

I started from two of my own templates that might be useful for others:

1. Azure Functions with FastAPI Demo at <https://github.com/AnsonLai/AzureFunctionFastAPIDemo>
2. Empty Template (210408) with Vue, jQuery, and Bootstrap at <https://jsfiddle.net/PharaohsVizier/rapoznhd/13/>

