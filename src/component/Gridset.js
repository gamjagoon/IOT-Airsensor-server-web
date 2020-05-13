import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Paper from "@material-ui/core/Paper";
import Grid from "@material-ui/core/Grid";
import Divider from "@material-ui/core/Divider";
import Weakdata from '../contents/Weakdata';
import Curdata from '../contents/Curdata';

const useStyles = makeStyles((theme) => ({
  container: {
    display: "grid",
    gridTemplateColumns: "repeat(12, 1fr)",
    gridGap: theme.spacing(12),
  },
  paper: {
    padding: theme.spacing(1),
    textAlign: "center",
    color: theme.palette.text.secondary,
    marginBottom: theme.spacing(1),
  },
  divider: {
    margin: theme.spacing(2, 0),
  },
}));

export default function Gridset() {
  const classes = useStyles();
  return (
    <div>
      <Divider className={classes.divider} />
      <Grid item sm={12} alignItems="center">
        <Paper className={classes.paper}>
          <Curdata />
        </Paper>
      </Grid>
      <Grid item sm={12} alignItems="center">
        <Paper className={classes.paper}>
          <Weakdata />
        </Paper>
      </Grid>
    </div>
  );
}