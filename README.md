# Test Case:

1. Open browser and select every available game category:  
  - Role-playing  
  - Simulation  
  - Indie  
  - Racing  
- Sports  
- Action  
- Strategy  
- Shooter  
- Adventure 
Check if current URL has game category name inside.    
At the end of test close browser.

2. Test steps: 

Program will:  
- automatically open we browser (Chrome)  
- iterate through every game type from menu dropdown called Genre — select every available game type from list and click on it  
- check if mark X beside Genre is visible  
- check if URL contains string with name of game type after every iteration  
3. Expectations:  
- there are available 9 games categories  
- every time when game category will be selected, URL has to contain this category as string in URL, e.g. after selected role playing category URL should be like this:  
https://www.gog.com/games/role-playing?sort=bestselling&page=1  
- after selected game category X mark beside menu dropdown Genre should be visible  
- web browser will be closed after the test 


# Dependencies:
- Chrome 59
https://www.google.com/chrome/browser/desktop/index.html

- ChromeDriver 2.30  
https://sites.google.com/a/chromium.org/chromedriver/

- Python 2.7.12    
https://www.python.org/downloads/

- Selenium 3.0.1   
<code>pip install selenium</code>  

- Robot Framework 3.0.2  
<code>pip install robotframework</code>  


# Run Robot Framework Test Case via terminal
- go to directory where Robot file is located in repository and run <code>robot gog.robot</code>
