#include <fann.h>
#include <sys/uio.h>
#include <linux/perf_event.h>
#include <stdlib.h>
#include <stdint.h>
#include <gmp.h>
#include <error.h>
#include <errno.h>
#include <assert.h>
#include <asc.h>

int asc_ssv_tstbit(ssv_t const *z, mp_bitcnt_t j)
{
    __mpz_struct const *Z;
    mp_bitcnt_t l;
    int i;

    for (i = 0; i < z->N; i++) {
        if (asc_ssv_lo(z, i) <= j && j < asc_ssv_hi(z, i)) {
            l = asc_ssv_mod(j, z, i);
            Z = z->sub[i].z;
            return mpz_tstbit(Z, l);
        }
    }

    assert(i < z->N);

    return 0;
}
