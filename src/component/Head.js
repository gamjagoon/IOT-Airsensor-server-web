import React from "react";
import Typography from "@material-ui/core/Typography";
import Grid from "@material-ui/core/Grid";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
  paper: {
    padding: theme.spacing(1),
    textAlign: "center",
    backgroundColor: "#ccefff",
    marginBottom: theme.spacing(1),
  },
}));

const Head = () => {
	const classes = useStyles();
	return (
    <Grid className={classes.paper}>
      <Typography variant="h3" gutterBottom>
        센서및 시스템 5조
      </Typography>
    </Grid>
  );
}

export default Head;