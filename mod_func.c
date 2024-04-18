#include <stdio.h>
#include "hocdec.h"
#define IMPORT extern __declspec(dllimport)
IMPORT int nrnmpi_myid, nrn_nobanner_;

modl_reg(){
	//nrn_mswindll_stdio(stdin, stdout, stderr);
    if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
	fprintf(stderr, "Additional mechanisms from files\n");

fprintf(stderr," Alpha_Synapse.mod");
fprintf(stderr," ampa.mod");
fprintf(stderr," ampaOLD.mod");
fprintf(stderr," gabaA.mod");
fprintf(stderr," gabaB3.mod");
fprintf(stderr," Gfluct2.mod");
fprintf(stderr," hsus.mod");
fprintf(stderr," Ik2.mod");
fprintf(stderr," Isodium.mod");
fprintf(stderr," kdr.mod");
fprintf(stderr," kdrtea.mod");
fprintf(stderr," kHT_VCN2003.mod");
fprintf(stderr," kLT_VCN2003.mod");
fprintf(stderr," nmda.mod");
fprintf(stderr," nmda2.mod");
fprintf(stderr, "\n");
    }
_Alpha_Synapse_reg();
_ampa_reg();
_ampaOLD_reg();
_gabaA_reg();
_gabaB3_reg();
_Gfluct2_reg();
_hsus_reg();
_Ik2_reg();
_Isodium_reg();
_kdr_reg();
_kdrtea_reg();
_kHT_VCN2003_reg();
_kLT_VCN2003_reg();
_nmda_reg();
_nmda2_reg();
}
