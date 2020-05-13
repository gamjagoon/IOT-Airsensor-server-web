import React from "react";
import Typography from "@material-ui/core/Typography";
import obj from "./pm_data/aqi.json";

const Curdata = () => {

	return (
    <div>
      <Typography variant="h4">
        PM2.5 : {obj[0].pm25.toFixed(2)}㎍/m³ <br />
        PM10 : {obj[0].pm10.toFixed(2)}㎍/m³
        <br />
        {obj[0].time}
      </Typography>
    </div>
  );
};

export default Curdata;
