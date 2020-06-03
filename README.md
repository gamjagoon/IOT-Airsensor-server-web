Fine-air sensor and serve using website
=============
# summary
## English
### 1. Hardware
 * main server : raspberryPi 3B+
 * fine-air sensor : SDS011 
### 2. Software
  * front-end : ejs
  * back-end 
    - server : nodejs(express)
    - sensing : python script
    - DB : sqlite3
    - data processing : javascript - char.js
## Korean
### 1. 하드웨어
 * 메인 서버 : raspberryPi 3B+
 * 미세먼지 센서 : SDS011 
### 2. 소프트웨어
  * 프론트-앤드 : ejs
  * 백-앤드
    - 서버 : nodejs(express)
    - 센서제어 : python script
    - 데이터 베이스 : sqlite3
    - 데이터 처리 : javascript - char.js
* * *
#### begin I haven't studied about web, server and DB so I should do studying those and setting up development environment
**~ 2020/05/11 : finished setting up sensor and DB**

**~ 2020/05/27 : rebuilded sqlite3 nodejs package which is 'better-sqlite3' and changed query syntex and code**
  ```js
    // delete these code
    var sqlite3 = require('sqlite3').verbose();
    var db = new sqlite3.Database('./pmdata.db');
    const sql = 'select * from data order by time desc limit 60'

    // put these code
    const sql = require('better-sqlite3')('./pmdata.db',{
      readonly : true
    });
    const rows = sql.prepare(`SELECT * FROM data order by rowid desc limit 60`).all();
    const rows2 = sql.prepare(`SELECT * FROM data where time like '% %:00' order by rowid desc limit 196`).all();
  ```
   think, syntax of better-sqlite3 is more useful and shorter than sqlite3 nodejs package that's why Javacript code is shter than python...and the other code !! 

**~ 2020/06/03 : routing funtion add my web server**

  ```js
    app.get('/tem',(req, res)=>{
      let rows = humsql.prepare(`SELECT * FROM hum order by rowid desc limit 60`).all();
      const curdata = rows[0];
      let hum = new Array(60);
      let tem = new Array(60);
      let time = new Array(60);
      rows = rows.reverse();
      for(let i = 0; i < 60; i++){
        hum[i] = rows[i].hum.toFixed(3);
        tem[i] = rows[i].tem.toFixed(3);
        time[i] = rows[i].time.slice(11,16);
      }
      res.render('index2',{
        curdata,
        hourdatas:{hum:hum,tem:tem,time:time},
      });
    });
  ```
  add humanity and temperature data view page
