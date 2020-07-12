import React from 'react';
import { Card, CardContent, Typography, Grid } from '@material-ui/core';
import cx from 'classnames';
import Badge from 'react-bootstrap/Badge'

import styles from './Cards.module.css';

const Info = ({ data: { infos, lastUpdate } }) => {
  if (!infos) {
    return 'Chargement...';
  }

  return (
    <div className={styles.container}>
      <Grid container spacing={3} justify="center">
        <Grid item xs={12} md={3} component={Card} className={cx(styles.card, styles.infected)}>
          <CardContent>
            <Typography color="textSecondary" gutterBottom>
              Infected
            </Typography>
            <Typography variant="h5" component="h2">
              {infos.totalCases} 
            </Typography>
            <Badge pill variant="primary">{infos.newCases}</Badge>
            <Typography color="textSecondary">
              {lastUpdate}
            </Typography>
            
            
            
          </CardContent>
        </Grid>
        <Grid item xs={12} md={3} component={Card} className={cx(styles.card, styles.recovered)}>
          <CardContent>
            <Typography color="textSecondary" gutterBottom>
              Recovered
            </Typography>
            <Typography variant="h5" component="h2">
              {infos.totalRecovered} 
            </Typography>
            <Badge pill variant="success">+ </Badge>
            <Typography color="textSecondary">
              {lastUpdate}
            </Typography>
          
          </CardContent>
        </Grid>
        <Grid item xs={12} md={3} component={Card} className={cx(styles.card, styles.activeCases)}>
          <CardContent>
            <Typography color="textSecondary" gutterBottom>
              Active Cases
            </Typography>
            <Typography variant="h5" component="h2">
              {infos.seriousCritical} 
            </Typography>
            <Badge pill variant="warning">{infos.activeCases}</Badge>
            <Typography color="textSecondary">
              {lastUpdate}
            </Typography>
          
          </CardContent>
        </Grid>
        <Grid item xs={12} md={3} component={Card} className={cx(styles.card, styles.deaths)}>
          <CardContent>
            <Typography color="textSecondary" gutterBottom>
              Deaths
            </Typography>
            <Typography variant="h5" component="h2">
            {infos.totalDeaths} 
            </Typography>
            <Badge pill variant="danger">{infos.newDeaths}</Badge>
            <Typography color="textSecondary">
              {lastUpdate}
            </Typography>
            
          </CardContent>
        </Grid>
      </Grid>
    </div>
  );
};
export default Info;
