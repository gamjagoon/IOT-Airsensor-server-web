import React from "react";
import Typography from "@material-ui/core/Typography";
import obj from "./pm_data/aqi.json";
//import fs from "fs";
//let obj = [];

const Curdata = () => {
//	fs.readFile('/var/www/html/aqi.json',(err, data)=>{
//		if(err){console.log(err);}
//		else{
//			obj= JSON.parse(data);
//		}
//	});
	return (
    <div>
      <Typography variant="h2">
        PM2.5 : {obj[0].pm25}㎍/m³ <br />
        PM10 : {obj[0].pm10}㎍/m³
        <br />
        {obj[0].time}
      </Typography>
    </div>
  );
};

export default Curdata;
