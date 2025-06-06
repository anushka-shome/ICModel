/* Created by Language version: 6.2.0 */
/* NOT VECTORIZED */
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
 
#define _threadargscomma_ /**/
#define _threadargs_ /**/
 	/*SUPPRESS 761*/
	/*SUPPRESS 762*/
	/*SUPPRESS 763*/
	/*SUPPRESS 765*/
	 extern double *getarg();
 static double *_p; static Datum *_ppvar;
 
#define t nrn_threads->_t
#define dt nrn_threads->_dt
#define E_e _p[0]
#define E_i _p[1]
#define g_e0 _p[2]
#define g_i0 _p[3]
#define std_e _p[4]
#define std_i _p[5]
#define tau_e _p[6]
#define tau_i _p[7]
#define i _p[8]
#define g_e _p[9]
#define g_i _p[10]
#define g_e1 _p[11]
#define g_i1 _p[12]
#define D_e _p[13]
#define D_i _p[14]
#define exp_e _p[15]
#define exp_i _p[16]
#define amp_e _p[17]
#define amp_i _p[18]
#define _g _p[19]
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
 /* external NEURON variables */
 /* declaration of user functions */
 static double _hoc_new_seed();
 static double _hoc_oup();
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
 _p = _prop->param; _ppvar = _prop->dparam;
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
 "new_seed", _hoc_new_seed,
 "oup", _hoc_oup,
 0, 0
};
#define new_seed new_seed_Gfluct2
 extern double new_seed();
 /* declare global and static user variables */
 /* some parameters have upper and lower limits */
 static HocParmLimits _hoc_parm_limits[] = {
 0,0,0
};
 static HocParmUnits _hoc_parm_units[] = {
 "E_e", "mV",
 "E_i", "mV",
 "g_e0", "umho",
 "g_i0", "umho",
 "std_e", "umho",
 "std_i", "umho",
 "tau_e", "ms",
 "tau_i", "ms",
 "i", "nA",
 "g_e", "umho",
 "g_i", "umho",
 "g_e1", "umho",
 "g_i1", "umho",
 "D_e", "umho umho /ms",
 "D_i", "umho umho /ms",
 0,0
};
 static double delta_t = 1;
 static double v = 0;
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
 
static int _ode_count();
 /* connect range variables in _p that hoc is supposed to know about */
 static char *_mechanism[] = {
 "6.2.0",
"Gfluct2",
 "E_e",
 "E_i",
 "g_e0",
 "g_i0",
 "std_e",
 "std_i",
 "tau_e",
 "tau_i",
 0,
 "i",
 "g_e",
 "g_i",
 "g_e1",
 "g_i1",
 "D_e",
 "D_i",
 0,
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
 	_p = nrn_prop_data_alloc(_mechtype, 20, _prop);
 	/*initialize range parameters*/
 	E_e = 0;
 	E_i = -75;
 	g_e0 = 0.0121;
 	g_i0 = 0.0573;
 	std_e = 0.003;
 	std_i = 0.0066;
 	tau_e = 2.728;
 	tau_i = 10.49;
  }
 	_prop->param = _p;
 	_prop->param_size = 20;
  if (!nrn_point_prop_) {
 	_ppvar = nrn_prop_datum_alloc(_mechtype, 2, _prop);
  }
 	_prop->dparam = _ppvar;
 	/*connect ionic variables to this model*/
 
}
 static _initlists();
 _Gfluct2_reg() {
	int _vectorized = 0;
  _initlists();
 	_pointtype = point_register_mech(_mechanism,
	 nrn_alloc,nrn_cur, nrn_jacob, nrn_state, nrn_init,
	 hoc_nrnpointerindex,
	 _hoc_create_pnt, _hoc_destroy_pnt, _member_func,
	 0);
 _mechtype = nrn_get_mechtype(_mechanism[1]);
  hoc_register_dparam_size(_mechtype, 2);
 	hoc_register_cvode(_mechtype, _ode_count, 0, 0, 0);
 	hoc_register_var(hoc_scdoub, hoc_vdoub, hoc_intfunc);
 	ivoc_help("help ?1 Gfluct2 /cygdrive/c/Users/labadmin/repos/ICModel/Gfluct2.mod\n");
 hoc_register_limits(_mechtype, _hoc_parm_limits);
 hoc_register_units(_mechtype, _hoc_parm_units);
 }
static int _reset;
static char *modelname = "Fluctuating conductances";

static int error;
static int _ninits = 0;
static int _match_recurse=1;
static _modl_cleanup(){ _match_recurse=1;}
static oup();
 
static int  oup (  )  {
   if ( tau_e  != 0.0 ) {
     g_e1 = exp_e * g_e1 + amp_e * normrand ( 0.0 , 1.0 ) ;
     }
   if ( tau_i  != 0.0 ) {
     g_i1 = exp_i * g_i1 + amp_i * normrand ( 0.0 , 1.0 ) ;
     }
    return 0; }
 
static double _hoc_oup(_vptr) void* _vptr; {
 double _r;
    _hoc_setdata(_vptr);
 _r = 1.;
 oup (  ) ;
 return(_r);
}
 
double new_seed (  _lseed )  
	double _lseed ;
 {
   double _lnew_seed;
 set_seed ( _lseed ) ;
   
/*VERBATIM*/
	  printf("Setting random generator with seed = %g\n", _lseed);
 
return _lnew_seed;
 }
 
static double _hoc_new_seed(_vptr) void* _vptr; {
 double _r;
    _hoc_setdata(_vptr);
 _r =  new_seed (  *getarg(1) ) ;
 return(_r);
}
 
static int _ode_count(_type)int _type; { hoc_execerror("Gfluct2", "cannot be used with CVODE");}

static void initmodel() {
  int _i; double _save;_ninits++;
 _save = t;
 t = 0.0;
{
 {
   g_e1 = 0.0 ;
   g_i1 = 0.0 ;
   if ( tau_e  != 0.0 ) {
     D_e = 2.0 * std_e * std_e / tau_e ;
     exp_e = exp ( - dt / tau_e ) ;
     amp_e = std_e * sqrt ( ( 1.0 - exp ( - 2.0 * dt / tau_e ) ) ) ;
     }
   if ( tau_i  != 0.0 ) {
     D_i = 2.0 * std_i * std_i / tau_i ;
     exp_i = exp ( - dt / tau_i ) ;
     amp_i = std_i * sqrt ( ( 1.0 - exp ( - 2.0 * dt / tau_i ) ) ) ;
     }
   }
  _sav_indep = t; t = _save;

}
}

static void nrn_init(_NrnThread* _nt, _Memb_list* _ml, int _type){
Node *_nd; double _v; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
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
 v = _v;
 initmodel();
}}

static double _nrn_current(double _v){double _current=0.;v=_v;{ {
   if ( tau_e  == 0.0 ) {
     g_e = std_e * normrand ( 0.0 , 1.0 ) ;
     }
   if ( tau_i  == 0.0 ) {
     g_i = std_i * normrand ( 0.0 , 1.0 ) ;
     }
   g_e = g_e0 + g_e1 ;
   if ( g_e < 0.0 ) {
     g_e = 0.0 ;
     }
   g_i = g_i0 + g_i1 ;
   if ( g_i < 0.0 ) {
     g_i = 0.0 ;
     }
   i = g_e * ( v - E_e ) + g_i * ( v - E_i ) ;
   }
 _current += i;

} return _current;
}

static void nrn_cur(_NrnThread* _nt, _Memb_list* _ml, int _type){
Node *_nd; int* _ni; double _rhs, _v; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
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
 _g = _nrn_current(_v + .001);
 	{ _rhs = _nrn_current(_v);
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

static void nrn_jacob(_NrnThread* _nt, _Memb_list* _ml, int _type){
Node *_nd; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
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

static void nrn_state(_NrnThread* _nt, _Memb_list* _ml, int _type){
 double _break, _save;
Node *_nd; double _v; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
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
 error =  oup();
 if(error){fprintf(stderr,"at line 152 in file Gfluct2.mod:\n	SOLVE oup\n"); nrn_complain(_p); abort_run(error);}
 
}}
 t = _save;
 }}}

}

static terminal(){}

static _initlists() {
 int _i; static int _first = 1;
  if (!_first) return;
_first = 0;
}
