import React from "react";
import Typography from "@material-ui/core/Typography";
import data from "./pm_data/data.json";

const Curdata = () => {
	return (
    <div>
      <Typography variant="h2">
        PM2.5 : {data[0].pm25}㎍/m³ <br />
        PM10 : {data[0].pm10}㎍/m³
        <br />
        {data[1].time}
      </Typography>
    </div>
  );
};

export default Curdata;
