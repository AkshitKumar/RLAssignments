/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

* File Name : aux_methods.cpp

* Purpose : Herd Management Assignment 

* Creation Date : 06-10-2013

* Last Modified : Sun 06 Oct 2013 05:17:24 AM IST

* Created By : npsabari

_._._._._._._._._._._._._._._._._._._._._.*/

#include "aux_methods.h"

double get_power(double a, int b) {
  double ret = 1.0;
  while(b--) {
    ret *= a;
  }
  return ret;
}

ll getnCr(int n, int r) {
  return factorial[n]/factorial[n-r]/factorial[r];
}

ppi get_split(int state_rep) {
  return mp(mp(state_rep/169, (state_rep%169)/13), (state_rep%169)%13);
}

void validation() {
  REP(i, MAX_STATE_NUMBER) {
    double sum = 0.0;
    REP(j, MAX_STATE_NUMBER) {
      sum += evolve_prob[i][j];
    }
    assert( sum > 1 - EPS && sum < 1 + EPS);
  }

  REP(i, MAX_STATE_NUMBER) {
    double sum = 0.0;
    REP(j, MAX_STATE_NUMBER) {
      sum += reproduction_prob[i][j];
    }
    assert( sum > 1 - EPS && sum < 1 + EPS);
  }

  REP(i, MAX_STATE_NUMBER) {
    double sum = 0.0;
    REP(j, MAX_STATE_NUMBER) {
      sum += afterstate_to_state[i][j];
    }
    assert( sum > 1 - EPS && sum < 1 + EPS);
  }
}


