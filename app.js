const express = require('express');
const path = require('path');
const sql = require('better-sqlite3')('./pmdata.db',{
  readonly : true
});
const humsql = require('better-sqlite3')('./humdata.db',{
  readonly : true
});
const aqi = require('./lib/aqi');
const app = express();
app.use('/static',express.static(path.join(__dirname,'static')));
app.set('view engine','ejs');

app.get('/',(req, res)=>{
  let rows = sql.prepare(`SELECT * FROM data order by rowid desc limit 60`).all().reverse();
  const rows2 = sql.prepare(`SELECT * FROM data where time like '% %:00' order by rowid desc limit 196`).all();
  const curdata = rows[59];
  let aqi_id = aqi.Get(curdata);
  let pm10 = new Array(60);
  let pm25 = new Array(60);
  let time = new Array(60);
  for (let i = 0; i < 60; i++) {
    pm10[i] = rows[i].pm10.toFixed(3);
    pm25[i] = rows[i].pm25.toFixed(3);
    time[i] = rows[i].time.slice(11,16);
  }
  let days = new Array(7);
  let aqis = new Array(7);
  let d = 0;
  let i = 195;
  while (d < 7) {
    let tmp = 0;
    days[d] = parseInt(rows2[i].time.slice(8,10),10);
    for (let j = 0; j < 24; j++) {
      tmp += aqi.Getaqi(rows2[i].pm25,rows2[i].pm10);
      i--;
    }
    aqis[d++] = parseInt((tmp/24).toFixed(0));
  }
  res.render('index',{
    data : {aqi: aqi_id[0],iconid: aqi_id[1]},
    curdata,
    hourdatas:{pm10:pm10,pm25:pm25,time:time},
    weakdata : {days:days,aqis:aqis}
  });
});

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


app.listen(30080, ()=>{
	console.log("start server");
});
