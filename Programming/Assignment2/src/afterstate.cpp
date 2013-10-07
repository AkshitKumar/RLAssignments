/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

* File Name : afterstate.cpp

* Purpose : Herd Management Assignment

* Creation Date : 02-10-2013

* Last Modified : Mon 07 Oct 2013 06:20:57 AM IST

* Created By : npsabari

_._._._._._._._._._._._._._._._._._._._._.*/

#include "afterstate.h"

afterstate::afterstate(int _num_young, int _num_breedable, int _num_old) 
  : state(_num_young, _num_breedable, _num_old)  {
  this->num_young = _num_young;
  this->num_breedable = _num_breedable;
  this->num_old = _num_old;
  this->total_cows = this->num_young + this->num_breedable + this->num_old;
}
