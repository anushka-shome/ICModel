/* Created by Language version: 6.2.0 */
/* VECTORIZED */
#include <stdio.h>
#include <math.h>
#include "scoplib.h"
#undef PI
 
#include "md1redef.h"
#include "section.h"
#include "md2redef.h"

#if METHOD3
extern int _method3;
#endif

#undef exp
#define exp hoc_Exp
extern double hoc_Exp();
 
#define _threadargscomma_ _p, _ppvar, _thread, _nt,
#define _threadargs_ _p, _ppvar, _thread, _nt
 	/*SUPPRESS 761*/
	/*SUPPRESS 762*/
	/*SUPPRESS 763*/
	/*SUPPRESS 765*/
	 extern double *getarg();
 /* Thread safe. No static _p or _ppvar. */
 
#define t _nt->_t
#define dt _nt->_dt
#define tauF _p[0]
#define tauR _p[1]
#define tauR2 _p[2]
#define a1 _p[3]
#define b1 _p[4]
#define tau _p[5]
#define tau1 _p[6]
#define tau2 _p[7]
#define e _p[8]
#define t1 _p[9]
#define t2 _p[10]
#define t3 _p[11]
#define t4 _p[12]
#define t5 _p[13]
#define t6 _p[14]
#define t7 _p[15]
#define t8 _p[16]
#define t9 _p[17]
#define t10 _p[18]
#define f1 _p[19]
#define f2 _p[20]
#define f3 _p[21]
#define f4 _p[22]
#define f5 _p[23]
#define f6 _p[24]
#define i _p[25]
#define g _p[26]
#define A _p[27]
#define B _p[28]
#define C _p[29]
#define D _p[30]
#define E _p[31]
#define F _p[32]
#define G _p[33]
#define H _p[34]
#define I _p[35]
#define J _p[36]
#define DA _p[37]
#define DB _p[38]
#define DC _p[39]
#define DD _p[40]
#define DE _p[41]
#define DF _p[42]
#define DG _p[43]
#define DH _p[44]
#define DI _p[45]
#define DJ _p[46]
#define v _p[47]
#define _g _p[48]
#define _tsav _p[49]
#define _nd_area  *_ppvar[0]._pval
 
#if MAC
#if !defined(v)
#define v _mlhv
#endif
#if !defined(h)
#define h _mlhh
#endif
#endif
 static int hoc_nrnpointerindex =  -1;
 static Datum* _extcall_thread;
 static Prop* _extcall_prop;
 /* external NEURON variables */
 extern double celsius;
 /* declaration of user functions */
 static int _mechtype;
extern int nrn_get_mechtype();
 extern Prop* nrn_point_prop_;
 static int _pointtype;
 static void* _hoc_create_pnt(_ho) Object* _ho; { void* create_point_process();
 return create_point_process(_pointtype, _ho);
}
 static void _hoc_destroy_pnt();
 static double _hoc_loc_pnt(_vptr) void* _vptr; {double loc_point_process();
 return loc_point_process(_pointtype, _vptr);
}
 static double _hoc_has_loc(_vptr) void* _vptr; {double has_loc_point();
 return has_loc_point(_vptr);
}
 static double _hoc_get_loc_pnt(_vptr)void* _vptr; {
 double get_loc_point_process(); return (get_loc_point_process(_vptr));
}
 static _hoc_setdata(_vptr) void* _vptr; { Prop* _prop;
 _prop = ((Point_process*)_vptr)->_prop;
 _extcall_prop = _prop;
 }
 /* connect user functions to hoc names */
 static IntFunc hoc_intfunc[] = {
 0,0
};
 static struct Member_func {
	char* _name; double (*_member)();} _member_func[] = {
 "loc", _hoc_loc_pnt,
 "has_loc", _hoc_has_loc,
 "get_loc", _hoc_get_loc_pnt,
 0, 0
};
 /* declare global and static user variables */
 /* some parameters have upper and lower limits */
 static HocParmLimits _hoc_parm_limits[] = {
 0,0,0
};
 static HocParmUnits _hoc_parm_units[] = {
 "tauF", "ms",
 "tauR", "ms",
 "tauR2", "ms",
 "tau", "ms",
 "tau1", "ms",
 "tau2", "ms",
 "e", "mV",
 "A", "nS",
 "B", "nS",
 "C", "nS",
 "D", "nS",
 "E", "nS",
 "F", "nS",
 "G", "nS",
 "H", "nS",
 "I", "nS",
 "J", "nS",
 "i", "nA",
 "g", "nS",
 0,0
};
 static double A0 = 0;
 static double B0 = 0;
 static double C0 = 0;
 static double D0 = 0;
 static double E0 = 0;
 static double F0 = 0;
 static double G0 = 0;
 static double H0 = 0;
 static double I0 = 0;
 static double J0 = 0;
 static double delta_t = 1;
 /* connect global user variables to hoc */
 static DoubScal hoc_scdoub[] = {
 0,0
};
 static DoubVec hoc_vdoub[] = {
 0,0,0
};
 static double _sav_indep;
 static void nrn_alloc(), nrn_init(), nrn_state();
 static void nrn_cur(), nrn_jacob();
 static void _hoc_destroy_pnt(_vptr) void* _vptr; {
   destroy_point_process(_vptr);
}
 
static int _ode_count(), _ode_map(), _ode_spec(), _ode_matsol();
 
#define _cvode_ieq _ppvar[2]._i
 /* connect range variables in _p that hoc is supposed to know about */
 static char *_mechanism[] = {
 "6.2.0",
"ICGABAb3",
 "tauF",
 "tauR",
 "tauR2",
 "a1",
 "b1",
 "tau",
 "tau1",
 "tau2",
 "e",
 "t1",
 "t2",
 "t3",
 "t4",
 "t5",
 "t6",
 "t7",
 "t8",
 "t9",
 "t10",
 "f1",
 "f2",
 "f3",
 "f4",
 "f5",
 "f6",
 0,
 "i",
 "g",
 0,
 "A",
 "B",
 "C",
 "D",
 "E",
 "F",
 "G",
 "H",
 "I",
 "J",
 0,
 0};
 
static void nrn_alloc(_prop)
	Prop *_prop;
{
	Prop *prop_ion, *need_memb();
	double *_p; Datum *_ppvar;
  if (nrn_point_prop_) {
	_prop->_alloc_seq = nrn_point_prop_->_alloc_seq;
	_p = nrn_point_prop_->param;
	_ppvar = nrn_point_prop_->dparam;
 }else{
 	_p = nrn_prop_data_alloc(_mechtype, 50, _prop);
 	/*initialize range parameters*/
 	tauF = 0.4157;
 	tauR = 45;
 	tauR2 = 13.34;
 	a1 = 1;
 	b1 = 19.98;
 	tau = 1026;
 	tau1 = 283;
 	tau2 = 112;
 	e = -85;
 	t1 = 215.78;
 	t2 = 419.07;
 	t3 = 28.706;
 	t4 = 51.68;
 	t5 = 65.056;
 	t6 = 29.17;
 	t7 = 42.772;
 	t8 = 80.711;
 	t9 = 41.132;
 	t10 = 42.585;
 	f1 = 2.2528;
 	f2 = 0.17354;
 	f3 = 17.074;
 	f4 = 10.71;
 	f5 = 3.1687;
 	f6 = 1.8296;
  }
 	_prop->param = _p;
 	_prop->param_size = 50;
  if (!nrn_point_prop_) {
 	_ppvar = nrn_prop_datum_alloc(_mechtype, 3, _prop);
  }
 	_prop->dparam = _ppvar;
 	/*connect ionic variables to this model*/
 
}
 static _initlists();
  /* some states have an absolute tolerance */
 static Symbol** _atollist;
 static HocStateTolerance _hoc_state_tol[] = {
 0,0
};
 static _net_receive();
 typedef (*_Pfrv)();
 extern _Pfrv* pnt_receive;
 extern short* pnt_receive_size;
 static _net_init();
 extern _Pfrv* pnt_receive_init;
 _gabaB3_reg() {
	int _vectorized = 1;
  _initlists();
 	_pointtype = point_register_mech(_mechanism,
	 nrn_alloc,nrn_cur, nrn_jacob, nrn_state, nrn_init,
	 hoc_nrnpointerindex,
	 _hoc_create_pnt, _hoc_destroy_pnt, _member_func,
	 1);
 _mechtype = nrn_get_mechtype(_mechanism[1]);
  hoc_register_dparam_size(_mechtype, 3);
 	hoc_register_cvode(_mechtype, _ode_count, _ode_map, _ode_spec, _ode_matsol);
 	hoc_register_tolerance(_mechtype, _hoc_state_tol, &_atollist);
 pnt_receive[_mechtype] = _net_receive;
 pnt_receive_init[_mechtype] = _net_init;
 pnt_receive_size[_mechtype] = 3;
 	hoc_register_var(hoc_scdoub, hoc_vdoub, hoc_intfunc);
 	ivoc_help("help ?1 ICGABAb3 /cygdrive/c/Users/labadmin/repos/ICModel/gabaB3.mod\n");
 hoc_register_limits(_mechtype, _hoc_parm_limits);
 hoc_register_units(_mechtype, _hoc_parm_units);
 }
static int _reset;
static char *modelname = "GABAb synapse";

static int error;
static int _ninits = 0;
static int _match_recurse=1;
static _modl_cleanup(){ _match_recurse=1;}
 
static int _ode_spec1(), _ode_matsol1();
 static int _slist1[10], _dlist1[10];
 static int state();
 
/*CVODE*/
 static int _ode_spec1 (double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt) {int _reset = 0; {
   DA = - A / t1 ;
   DB = - B / t2 ;
   DC = - C / t3 ;
   DD = - D / t4 ;
   DE = - E / t5 ;
   DF = - F / t6 ;
   DG = - G / t7 ;
   DH = - H / t8 ;
   DI = - I / t9 ;
   DJ = - J / t10 ;
   }
 return _reset;
}
 static int _ode_matsol1 (double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt) {
 DA = DA  / (1. - dt*( ( - 1.0 ) / t1 )) ;
 DB = DB  / (1. - dt*( ( - 1.0 ) / t2 )) ;
 DC = DC  / (1. - dt*( ( - 1.0 ) / t3 )) ;
 DD = DD  / (1. - dt*( ( - 1.0 ) / t4 )) ;
 DE = DE  / (1. - dt*( ( - 1.0 ) / t5 )) ;
 DF = DF  / (1. - dt*( ( - 1.0 ) / t6 )) ;
 DG = DG  / (1. - dt*( ( - 1.0 ) / t7 )) ;
 DH = DH  / (1. - dt*( ( - 1.0 ) / t8 )) ;
 DI = DI  / (1. - dt*( ( - 1.0 ) / t9 )) ;
 DJ = DJ  / (1. - dt*( ( - 1.0 ) / t10 )) ;
}
 /*END CVODE*/
 static int state (double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt) { {
    A = A + (1. - exp(dt*(( - 1.0 ) / t1)))*(- ( 0.0 ) / ( ( - 1.0 ) / t1 ) - A) ;
    B = B + (1. - exp(dt*(( - 1.0 ) / t2)))*(- ( 0.0 ) / ( ( - 1.0 ) / t2 ) - B) ;
    C = C + (1. - exp(dt*(( - 1.0 ) / t3)))*(- ( 0.0 ) / ( ( - 1.0 ) / t3 ) - C) ;
    D = D + (1. - exp(dt*(( - 1.0 ) / t4)))*(- ( 0.0 ) / ( ( - 1.0 ) / t4 ) - D) ;
    E = E + (1. - exp(dt*(( - 1.0 ) / t5)))*(- ( 0.0 ) / ( ( - 1.0 ) / t5 ) - E) ;
    F = F + (1. - exp(dt*(( - 1.0 ) / t6)))*(- ( 0.0 ) / ( ( - 1.0 ) / t6 ) - F) ;
    G = G + (1. - exp(dt*(( - 1.0 ) / t7)))*(- ( 0.0 ) / ( ( - 1.0 ) / t7 ) - G) ;
    H = H + (1. - exp(dt*(( - 1.0 ) / t8)))*(- ( 0.0 ) / ( ( - 1.0 ) / t8 ) - H) ;
    I = I + (1. - exp(dt*(( - 1.0 ) / t9)))*(- ( 0.0 ) / ( ( - 1.0 ) / t9 ) - I) ;
    J = J + (1. - exp(dt*(( - 1.0 ) / t10)))*(- ( 0.0 ) / ( ( - 1.0 ) / t10 ) - J) ;
   }
  return 0;
}
 
static _net_receive (_pnt, _args, _lflag) Point_process* _pnt; double* _args; double _lflag; 
{  double* _p; Datum* _ppvar; Datum* _thread; _NrnThread* _nt;
   _thread = (Datum*)0; _nt = (_NrnThread*)_pnt->_vnt;   _p = _pnt->_prop->param; _ppvar = _pnt->_prop->dparam;
  if (_tsav > t){ extern char* hoc_object_name(); hoc_execerror(hoc_object_name(_pnt->ob), ":Event arrived out of order. Must call ParallelContext.set_maxstep AFTER assigning minimum NetCon.delay");}
 _tsav = t; {
   double _ltd , _ltd2 ;
 _ltd = ( t - _args[1] ) ;
   _ltd2 = ( t - _args[2] ) ;
   if ( _ltd > 0.0 ) {
     A = A + .001 * _args[0] * ( 1.0 - ( a1 * exp ( - _ltd / tauR ) - a1 * exp ( - _ltd / tauF ) ) ) ;
     B = B + .001 * _args[0] * ( 1.0 - ( a1 * exp ( - _ltd / tauR ) - a1 * exp ( - _ltd / tauF ) ) ) ;
     C = C + .001 * _args[0] * ( 1.0 - ( a1 * exp ( - _ltd / tauR ) - a1 * exp ( - _ltd / tauF ) ) ) ;
     D = D + .001 * _args[0] * ( 1.0 - ( a1 * exp ( - _ltd / tauR ) - a1 * exp ( - _ltd / tauF ) ) ) ;
     E = E + .001 * _args[0] * ( 1.0 - ( a1 * exp ( - _ltd / tauR ) - a1 * exp ( - _ltd / tauF ) ) ) ;
     F = F + .001 * _args[0] * ( 1.0 - ( a1 * exp ( - _ltd / tauR ) - a1 * exp ( - _ltd / tauF ) ) ) ;
     G = G + .001 * _args[0] * ( 1.0 - ( a1 * exp ( - _ltd / tauR ) - a1 * exp ( - _ltd / tauF ) ) ) ;
     H = H + .001 * _args[0] * ( 1.0 - ( a1 * exp ( - _ltd / tauR ) - a1 * exp ( - _ltd / tauF ) ) ) ;
     I = I + .001 * _args[0] * ( 1.0 - ( a1 * exp ( - _ltd / tauR ) - a1 * exp ( - _ltd / tauF ) ) ) ;
     J = J + .001 * _args[0] * ( 1.0 - ( a1 * exp ( - _ltd / tauR ) - a1 * exp ( - _ltd / tauF ) ) ) ;
     }
   else if ( _ltd2 > 0.0 ) {
     A = A + .001 * _args[0] * ( 1.0 - ( exp ( - _ltd / tauR ) - exp ( - _ltd / tauF ) ) * ( 1.0 + b1 * exp ( - _ltd2 / tauR2 ) ) ) ;
     B = B + .001 * _args[0] * ( 1.0 - ( exp ( - _ltd / tauR ) - exp ( - _ltd / tauF ) ) * ( 1.0 + b1 * exp ( - _ltd2 / tauR2 ) ) ) ;
     C = C + .001 * _args[0] * ( 1.0 - ( exp ( - _ltd / tauR ) - exp ( - _ltd / tauF ) ) * ( 1.0 + b1 * exp ( - _ltd2 / tauR2 ) ) ) ;
     D = D + .001 * _args[0] * ( 1.0 - ( exp ( - _ltd / tauR ) - exp ( - _ltd / tauF ) ) * ( 1.0 + b1 * exp ( - _ltd2 / tauR2 ) ) ) ;
     E = E + .001 * _args[0] * ( 1.0 - ( exp ( - _ltd / tauR ) - exp ( - _ltd / tauF ) ) * ( 1.0 + b1 * exp ( - _ltd2 / tauR2 ) ) ) ;
     F = F + .001 * _args[0] * ( 1.0 - ( exp ( - _ltd / tauR ) - exp ( - _ltd / tauF ) ) * ( 1.0 + b1 * exp ( - _ltd2 / tauR2 ) ) ) ;
     G = G + .001 * _args[0] * ( 1.0 - ( exp ( - _ltd / tauR ) - exp ( - _ltd / tauF ) ) * ( 1.0 + b1 * exp ( - _ltd2 / tauR2 ) ) ) ;
     H = H + .001 * _args[0] * ( 1.0 - ( exp ( - _ltd / tauR ) - exp ( - _ltd / tauF ) ) * ( 1.0 + b1 * exp ( - _ltd2 / tauR2 ) ) ) ;
     I = I + .001 * _args[0] * ( 1.0 - ( exp ( - _ltd / tauR ) - exp ( - _ltd / tauF ) ) * ( 1.0 + b1 * exp ( - _ltd2 / tauR2 ) ) ) ;
     J = J + .001 * _args[0] * ( 1.0 - ( exp ( - _ltd / tauR ) - exp ( - _ltd / tauF ) ) * ( 1.0 + b1 * exp ( - _ltd2 / tauR2 ) ) ) ;
     }
   else {
     A = A + .001 * _args[0] ;
     B = B + .001 * _args[0] ;
     C = C + .001 * _args[0] ;
     D = D + .001 * _args[0] ;
     E = E + .001 * _args[0] ;
     F = F + .001 * _args[0] ;
     G = G + .001 * _args[0] ;
     H = H + .001 * _args[0] ;
     I = I + .001 * _args[0] ;
     J = J + .001 * _args[0] ;
     }
   _args[2] = _args[1] ;
   _args[1] = t ;
   } }
 
static _net_init(_pnt, _args, _lflag) Point_process* _pnt; double* _args; double _lflag; {
       double* _p = _pnt->_prop->param;
    Datum* _ppvar = _pnt->_prop->dparam;
    Datum* _thread = (Datum*)0;
    _NrnThread* _nt = (_NrnThread*)_pnt->_vnt;
 _args[1] = t ;
   _args[2] = t ;
   }
 
static int _ode_count(_type) int _type;{ return 10;}
 
static int _ode_spec(_NrnThread* _nt, _Memb_list* _ml, int _type) {
   double* _p; Datum* _ppvar; Datum* _thread;
   Node* _nd; double _v; int _iml, _cntml;
  _cntml = _ml->_nodecount;
  _thread = _ml->_thread;
  for (_iml = 0; _iml < _cntml; ++_iml) {
    _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
    _nd = _ml->_nodelist[_iml];
    v = NODEV(_nd);
     _ode_spec1 (_p, _ppvar, _thread, _nt);
 }}
 
static int _ode_map(_ieq, _pv, _pvdot, _pp, _ppd, _atol, _type) int _ieq, _type; double** _pv, **_pvdot, *_pp, *_atol; Datum* _ppd; { 
	double* _p; Datum* _ppvar;
 	int _i; _p = _pp; _ppvar = _ppd;
	_cvode_ieq = _ieq;
	for (_i=0; _i < 10; ++_i) {
		_pv[_i] = _pp + _slist1[_i];  _pvdot[_i] = _pp + _dlist1[_i];
		_cvode_abstol(_atollist, _atol, _i);
	}
 }
 
static int _ode_matsol(_NrnThread* _nt, _Memb_list* _ml, int _type) {
   double* _p; Datum* _ppvar; Datum* _thread;
   Node* _nd; double _v; int _iml, _cntml;
  _cntml = _ml->_nodecount;
  _thread = _ml->_thread;
  for (_iml = 0; _iml < _cntml; ++_iml) {
    _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
    _nd = _ml->_nodelist[_iml];
    v = NODEV(_nd);
 _ode_matsol1 (_p, _ppvar, _thread, _nt);
 }}

static void initmodel(double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt) {
  int _i; double _save;{
  A = A0;
  B = B0;
  C = C0;
  D = D0;
  E = E0;
  F = F0;
  G = G0;
  H = H0;
  I = I0;
  J = J0;
 {
   A = 0.0 ;
   B = 0.0 ;
   C = 0.0 ;
   D = 0.0 ;
   E = 0.0 ;
   F = 0.0 ;
   G = 0.0 ;
   H = 0.0 ;
   I = 0.0 ;
   J = 0.0 ;
   }
 
}
}

static void nrn_init(_NrnThread* _nt, _Memb_list* _ml, int _type){
double* _p; Datum* _ppvar; Datum* _thread;
Node *_nd; double _v; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
_thread = _ml->_thread;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
 _tsav = -1e20;
#if CACHEVEC
  if (use_cachevec) {
    _v = VEC_V(_ni[_iml]);
  }else
#endif
  {
    _nd = _ml->_nodelist[_iml];
    _v = NODEV(_nd);
  }
 v = _v;
 initmodel(_p, _ppvar, _thread, _nt);
}}

static double _nrn_current(double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt, double _v){double _current=0.;v=_v;{ {
   g = f1 * A + f2 * B + f1 * C + f3 * D - f4 * E + f2 * F + f5 * G - f6 * H - f4 * I - f6 * J ;
   i = g * ( v - e ) ;
   }
 _current += i;

} return _current;
}

static void nrn_cur(_NrnThread* _nt, _Memb_list* _ml, int _type) {
double* _p; Datum* _ppvar; Datum* _thread;
Node *_nd; int* _ni; double _rhs, _v; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
_thread = _ml->_thread;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
#if CACHEVEC
  if (use_cachevec) {
    _v = VEC_V(_ni[_iml]);
  }else
#endif
  {
    _nd = _ml->_nodelist[_iml];
    _v = NODEV(_nd);
  }
 _g = _nrn_current(_p, _ppvar, _thread, _nt, _v + .001);
 	{ _rhs = _nrn_current(_p, _ppvar, _thread, _nt, _v);
 	}
 _g = (_g - _rhs)/.001;
 _g *=  1.e2/(_nd_area);
 _rhs *= 1.e2/(_nd_area);
#if CACHEVEC
  if (use_cachevec) {
	VEC_RHS(_ni[_iml]) -= _rhs;
  }else
#endif
  {
	NODERHS(_nd) -= _rhs;
  }
 
}}

static void nrn_jacob(_NrnThread* _nt, _Memb_list* _ml, int _type) {
double* _p; Datum* _ppvar; Datum* _thread;
Node *_nd; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
_thread = _ml->_thread;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml];
#if CACHEVEC
  if (use_cachevec) {
	VEC_D(_ni[_iml]) += _g;
  }else
#endif
  {
     _nd = _ml->_nodelist[_iml];
	NODED(_nd) += _g;
  }
 
}}

static void nrn_state(_NrnThread* _nt, _Memb_list* _ml, int _type) {
 double _break, _save;
double* _p; Datum* _ppvar; Datum* _thread;
Node *_nd; double _v; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
_thread = _ml->_thread;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
 _nd = _ml->_nodelist[_iml];
#if CACHEVEC
  if (use_cachevec) {
    _v = VEC_V(_ni[_iml]);
  }else
#endif
  {
    _nd = _ml->_nodelist[_iml];
    _v = NODEV(_nd);
  }
 _break = t + .5*dt; _save = t;
 v=_v;
{
 { {
 for (; t < _break; t += dt) {
   state(_p, _ppvar, _thread, _nt);
  
}}
 t = _save;
 }}}

}

static terminal(){}

static _initlists(){
 double _x; double* _p = &_x;
 int _i; static int _first = 1;
  if (!_first) return;
 _slist1[0] = &(A) - _p;  _dlist1[0] = &(DA) - _p;
 _slist1[1] = &(B) - _p;  _dlist1[1] = &(DB) - _p;
 _slist1[2] = &(C) - _p;  _dlist1[2] = &(DC) - _p;
 _slist1[3] = &(D) - _p;  _dlist1[3] = &(DD) - _p;
 _slist1[4] = &(E) - _p;  _dlist1[4] = &(DE) - _p;
 _slist1[5] = &(F) - _p;  _dlist1[5] = &(DF) - _p;
 _slist1[6] = &(G) - _p;  _dlist1[6] = &(DG) - _p;
 _slist1[7] = &(H) - _p;  _dlist1[7] = &(DH) - _p;
 _slist1[8] = &(I) - _p;  _dlist1[8] = &(DI) - _p;
 _slist1[9] = &(J) - _p;  _dlist1[9] = &(DJ) - _p;
_first = 0;
}
