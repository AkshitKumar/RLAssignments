/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

* File Name : state.cpp

* Purpose : Herd Management Assignment

* Creation Date : 02-10-2013

* Last Modified : Sun 06 Oct 2013 04:29:29 AM IST

* Created By : npsabari

_._._._._._._._._._._._._._._._._._._._._.*/

#include "state.h"

state::state(int _num_young, int _num_breedable, int _num_old) {
  this->num_young = _num_young;
  this->num_breedable = _num_breedable;
  this->num_old = _num_old;
  this->total_cows = this->num_young + this->num_breedable + this->num_old;
}

int state::get_state_rep() {
  return compress_naming[this->num_young*169 + this->num_breedable*13 + this->num_old];
}
