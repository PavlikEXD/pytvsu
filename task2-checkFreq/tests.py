import unittest
from solution import solution

class CheckFreqSimpleTests(unittest.TestCase):
    def test1(self):
        assert solution('Hello World!') == 'l'

    def test2(self):
        assert solution('How do you do') == 'o'

    def test3(self):
        assert solution('One') == 'e'

    def test4(self):
        assert solution('Oops!') == 'o'

    def test5(self):
        assert solution('AAaooo!!!!') == 'a'

    def test6(self):
        assert solution('abe') == 'a'


class CheckFreqBasicTests(unittest.TestCase):
    def test1(self):
        assert solution('Lorem ipsum dolor sit amet!') == 'm'

    def test2(self):
        assert solution('Lorem ipsum dolor sit amet 0000000000000000000') == 'm'

    def test3(self):
        assert solution('Aaaaaaaaaaaaaaaa!!!!') == 'a'

    def test4(self):
        assert solution('Gregor then turned to look out the window at the dull weather.Nooooooooooo!!! Why!?!') == 'o'

    def test5(self):
        assert solution('fn;lsfndasl;f naslkdnlkasdnfslahwemwjkrjkl;zcmk;lzcdkcslksdkseewme,') == 'k'

    def test6(self):
        assert solution('fsbd') == 'b'

class CheckFreqTextTests(unittest.TestCase):
    def test1(self):
        assert solution(
"""
The quick, brown fox jumps over a lazy dog.
DJs flock by when MTV ax quiz prog. 
Junk MTV quiz graced by fox whelps. 
Bawds jog, flick quartz, vex nymphs. 
Waltz, bad nymph, for quick jigs vex! 
Fox nymphs grab quick-jived waltz. 
Brick quiz whangs jumpy veldt fox. 
Bright vixens jump; dozy fowl quack. 
Quick wafting zephyrs vex bold Jim. 
Quick zephyrs blow, vexing daft Jim. 
Sex-charged fop blew my junk TV quiz. 
How quickly daft jumping zebras vex. 
Two driven jocks help fax my big quiz.
""") == 'i'

    def test2(self):
        assert solution(
"""
But I must explain to you how all this mistaken idea of denouncing pleasure 
and praising pain was born and I will give you a complete account of the system, 
and expound the actual teachings of the great explorer of the truth, 
the master-builder of human happiness.
""") == 'e'

    def test3(self):
        assert solution(
"""
One morning, when Gregor Samsa woke from troubled dreams, 
he found himself transformed in his bed into a horrible vermin. 
He lay on his armour-like back, and if he lifted his head a little 
he could see his brown belly, slightly domed and divided by arches 
into stiff sections. The bedding was hardly able to cover it and 
seemed ready to slide off any moment. His many legs, pitifully thin 
compared with the size of the rest of him, waved about helplessly as he looked.
""") == 'e'

class CheckFreqSimpleTests(unittest.TestCase):
    def test1(self):
        assert solution('a' * 10000) == 'a'

    def test2(self):
        assert solution('Z') == 'z'

    def test3(self):
        assert solution('a-z') == 'a'

    def test4(self):
        assert solution('A-Z') == 'a'

    def test5(self):
        assert solution('      d       ') == 'd'

    def test6(self):
        assert solution('i-d-d-q-d') == 'd'

    def test7(self):
        assert solution('ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba') == 'a'

    def test8(self):
        assert solution('12345,12345,12345 S 12345,12345') == 's'

    def test9(self):
        assert solution(
            'GnBnXOUoFCsDGZbCuGdWbDGBPRSxkTypOUtFQxGUvbnwJIDCrsqEBEvidEbYdFOdiPyQDUDKgZ'
            'ScxARtsxAcJHflnbYvqphyVrDtfoBCvCnaVPlEyEWINxtkjYESWPpgDldlynMtaHoRskFcVTQx'
            'MrECVdoCfmMLWTwcHEWNqEFZkQiGtofWbrxeIPgHHFaERzIoscciNSnaAWAAVIDRWtjAnQnAVM'
            'xRftIIFjgJVtpvVGNnSRFXarcWoriGiBDWvMxyYwJPaxKsOsndxdSVozHRHMuTrHlHseXTfbVv'
            'fSWwkWNYtWtbGiyoxhjkactDuVgwihmgqbCJyYnRXfsfwkJKuFWIDJSLUXFYjzUvTlZECLHumR'
            'VWdVtTBzztrbrECLYipUkufiHjxdjYsRFsGuuAEuZrDoIMcegTsVAYcWqgxlmMxepqxXOhIeQL'
            'qWcZsvxFqfXEKYwgdiCenMVTajwrfClyxEIElvaJZsoiTlRdJDTjqYVdDdItQpChjGRmrOLzJg'
            'zFuwXiaITZnZnAbPFUjWUqWROyMnLbygLBeNxiqtFkieRbxqaKTuDwEFpySfdFkgjzvbZKVkmY'
            'qIJVkAVWsFMpjOSKGrARYJAOPBDCysyhqjtdiPfwhMbFVtHRwHfxXeJuGfOvlKJFdixygpmrbV'
            'vtZcGDTDOpxTAKvdNVLdDGeNYxarGmQSlgpbaSMygTScTjLyOiOlvbhRoHFVGizXfYVuoTEfiO'
            'UMbadYRDUFmpayuuZnsTrpxnhQCXUrtTNcydISpHLFUeHVZBwarRZtfbmiZEqwXowvvbiVanah'
            'sTcwnTsbhcVfDPWmrxduDCpeHMBjudkUrtkdMbrugnzYnBEfssoYuRxZlGjzmorCfPbVQuUCzK'
            'mVQeeVcDajfLrGfSMioorxkBpMMqznnACQTSgzpWBlvEeqyRrVUraeieVzTVDKZKJfJFYAXacf'
            'jdjeRJndlPdObSUYsoxVkFzyXRHGKvYaIrOCwbnsVsrMryCBHwBOAohslTfXhnJbKehTVXULRj'
            'kRyRyuEMmcrJDiUErpCSIRRVZosPQCyblsAvwiaWnWmVuFjJEBnDtWyJQqNjbTZoPZiwBQBgzn'
            'tBmsMxUtKzeeDbxQoCoXQyFCbGHOcQDSfocCWXltTjHmtPvLptPoppedROYprjxiIEAolIKKOg'
            'dAWJBjFIOPKktcrQJCiUlEjFkwwQhouWCnIzERhCxNHyuotLrRpEWCagbBMsnWAgFUcXpWydVi'
            'OUfkKzedTKcPCHMiqsZCrOtRAeDNLZwyRArTGgvNnDxSOMyaotuEANGxaUiBYiNkmGlVNPdmol'
            'FdPcNkZPmFrVVRymCAzKtrKphvXqSRPwVzqnmqabVxfUbJgBHEBuNYdNjDvMmPWgPlruZPTPdT'
            'hlWPJJSrIHfgMvsMkJCCauqoUUyGmbJIXNIgPqDXpWhJJPQpYamgRSyohOHgDPFFELyKddnYVW'
            'cTSnstfeSeMspbnbVPMpXdLodnHYIztOGEvXrjiGZxTufUoehoiigjeDRBcNUUdvzXkYERjZGl'
            'TqkyouUjtKgbFVdSDgjTxUKWQoDGmqWIvvAUoCfXsQWinfgFadyEFDvXmxQVNbBlHASTdykcdW'
            'yjSBxnKYrUoRQnnhOHNVSOIEdVwELMEBwqiZvNFOFEFpUCHXAeUNlkwhHxAgVuCzlNLwDNBmNl'
            'dPNAaYfMJtZpIhwqVeeatOLXUXbIvKtIRDNqTIAMExadacKaLpVjyYIQdFbgaRJspZHspqgaty'
            'KcZDcVwejhiYRBWmhSfnkrbTJCHGCOcUhwIjRiJZcNxJIirhPnKwOorfjpyvCVssMBBjRRnZvz'
            'KBTSrqgcFpfxJIGqQdkKENPnBuEaAaQxabPCReaVCcEwghRGZuwSrqPbuhtVlinBSKdSMPPzMC'
            'TAHmLTTUOlshssIkbrLXkWgyDPzsjsQzTboqBibABnsujgXYmSmgVrBxPrvMYqXAPjZarpWhvc'
            'nLoqyPteFCMIXomQhGVCuyhfbullXxYGnxSkuAFmlIbetOcHmvEskUibIPvhBZAdKVhZRRaEfl'
            'ppJxAraKAZdGUtsGqTXNqJWYWtXNwTQpKbVUXBkMjsYnArGsyzajwXpsGRItHggoQsqiPrsUht'
            'VFPIxJelpvYjjYJEHnAyKsbxeVRkDUfPFidJVwDfDecuLzizVDtOLfBJOJrcXtJuRnwhpbBtcf'
            'qCgUojAqNEaqJGspXIVEwPHvdpSuggHhbfjbTmvOcHDszZWqwGUpZunPTcDlWbzOmRVVcKqxnN'
            'XHrKfVcYyXDTdcKviFDmYAwZWnehpxvaSjGrTvpClxsHlRlYfXAUMPFGQCJmQhtJmcRvtBIHJU'
            'WfSDFwuuMBnIkFEHbPbjskgutNnFPmWJSvKzKyYHYANonjhJHJjzpsDUGPYVsyFZEWopUQeaai'
            'wiZJhCtBesdBGAJMINcmEOqrfoktmgiATgTrwYHDBtxefDeAaynWIhQDImGzsOxRrXOJVOJQpG'
            'wdUOSSaqwSQVahOQgejaJkjhZrfxxuidKanZZrnXaTpwCJlEvPYGrsxWbJNpssuntxPdTiwQqs'
            'KiLPZaQLZCnLesAfmWXOdLrIupKAicAqLAloGrVBcjBTpSlWcxfIbyvXtILmZubGdayxMJEcBG'
            'zuqHuTWICNiWxKeRdDUPjrvwHAXWPinABwqotUVbwNRGkaLbVyDVEljAFRunkWAGtkUeOSHiTY'
            'MCrcOTVEmGVlDhaYkPnaFOMYcmRuWrpOLcLfkrJozBKcxyoZyAHKiuvGfMXuXfakotREMztCxl'
            'SldEugLHsahoGAksljttJBlwkTsRQaTwHhjQVmpIjFiBrizYYKMrrQpTUoVyZWxViAYDahpiYi'
            'wqweyvKvTFnNpsYEsAcTSJNpNhBcbZMNzsRENFkTNZrXFkBiVghbtwNkKyRlxPFJYhZOPAwwkM'
            'mdNfkEFEwcscRXVjHyqefRSxBdzfmsoMoMCLWYgtzlziNsznnOtXcXtXcBRAQKVbVuUgICEnZF'
            'AsDdMCLUUhtixwnElONEMysVJgJzAGIUBCjqDGRjQsmqaAREqkxdTOhlzmWsJtnTCuDEwpkDhz'
            'vTboqCsBFOLSvLIsvTOVxRqgdzfrlYjUZkWGQfeLMzRDDkSktRDzzxxAZOkKbrksZIinVvCdkH'
            'bqUhRQCRKBOPuKhiqVyVFVcvjpaqdWMtBzJpDNcOptquTuERwkIsdaDBnkWWuPVlkEbnVbRaOg'
            'iVPkihUlUpjxayHeDkPtdSVNAeFzoXFIXvngPkAzCffUtZepNCfcyGshoXItlaAEFxCEMZfEnO'
            'ySwcEXqCAtXvHkHmwDOwItXUoCCMgDQEoagyMvNLZKYGcdnowMJcADbjYyGbNRXVNJnjMhoKLa'
            'jccsPlykgfGBzJnegcFjnmwdoVumnxlDhiRKMGgLWSaWmTUYJGMLPIEyexNReQthWJwPZPsRjy'
            'QzqpqcDKqleSevWBSTzigPXwraKvbJrXZYTLIZqfyCfqoQjWyhCLpvsxqYqeigMnxwdxmHwCzV'
            'epaWjomQBtGdpmqAaUlvOZeEkqyUpWCvgiPjgyVMwhJWsoTnvUmrekccjNajTQjfcwQWKkNtza'
            'ORVTEctrhvETrAoEINzYOpeuSGqlcFrlWndQeaPSnifGRyvZKCkDbbSVrwfChzGzmVeXgrlkuZ'
            'WrPCpJQCsnGvurlUvYxTxvDSNolZmpCDOVCyaXvkddSQXHjKQuPIrWTbwQxqhxZFrrkIRZMphx'
            'gJEbEhNRcucOpBuDzZrOMzgnvMLvJKqjhBAynSHAomYrhaNYWxIsNNeCVkGOKkXkZwOfTsQIMc'
            'OlXMuUZVZhqyiSJbZyEghiVVEyVXSQFbFDMWxYDPPEWDnsUegeyhGOccSQvbYVDGOWDHaHjYsv'
            'MHGxQrujPYVtbsYekHAkCkoXEMzhBwzsxuVxHTjwtpckpEAeAlpibYrOpYNGqqIFIuHeHDlWVd'
            'ZacgsjJjGVrruQfacCtuJmKhcNAIQTlynPFXaNwzVWhwbYCgNwhTICANByCoBCfWoihbQqYAZZ'
            'MJDpdemZRLHrbNwXtBHMekykiMfCPYYFzlYaXPlSqYsHOcAYYzppTsijEwWyazkiWIQHapufrm'
            'GLQQrnWGuITZVuayCNjnumdRwJYzHpFellmGIOCLUyXlzZlXxmBYUyslIRCqyQpJOrDwmnVCck'
            'KntGiliVmTfFixPlHcGoeLzeEGsfVxofwWirJhDkSOpFHsFNZOtTHTIaElsMgOKowUQWBjesJB'
            'bsACowVGxxXIoLmCyXdRIvbTpIfNEsstmulOXfOCSCenFNFFNhVKOcSpgjnZKgfAIRiWcCDYvi'
            'aygzYtTEnWGHWeUPTRrKaxlyTVPLONSgeqhfcwpLeCJxQNFvpktPNZxkqGqmETAynMCwDIAVVL'
            'jFmTPpPQWzkeVHBXIJrazRnAeAABDNQqKVRWDZdDFIdFJdwDSlCBlfWfMXiyWejnuIUaPGUFov'
            'NtNxRFqCfHOVvtDRNrUJlunBktaoRSYNcZVQjWzoTnPLlluGfyHNVQjZtrlHOBbrNebbVMenwD'
            'EHggshFHqkiYnyFpRjzoVTfPLPjUkhzXbqOWOhDzVsYhofjDzEohyGWSixIuzdjvvrZxmyejrI'
            'svjrMQRlnMBrzDQcmHvoXQOXkthGlRGJFtjgwmrDFyoKuBSkYtWtcpaPkGYiPMHsRmjBqRDewf'
            'YSmEkmcYGQLQstZhlhzQgFEwZbjKmeLdnXqWvihWoIOWILtbDwlmWerPZuLFVTIMNAVoMWoiqg'
            'ubaFgjeKCeFavnzzXHNSjZREIHptwZusEpjxdKIZasCDDicRvTFpfGhpsogepdaIflrRAMspuo'
            'MNqTcptNqTLtmbRWbOpYlChvKYmseVszigNvkeVHexeBmasSTAttSaadvWCBtJxISChsIGClKL'
            'tgqARMCECQcKCNgTfOpnyVDnNticYnmSotFGOtiWYVodwhmWyXzxHhFYiKnwhoBVcTGhJUvFPn'
            'YiUpeToNlQDwzhWdwEZuvpnFqqvFWZfSSrhJzMFfwhkAQnZxOJaDYapzgYICsrCVWGEcVFFjkN'
            'QjUhztuiIcuPGQcEAjleDQBKMdggjnDpJBHYDYaKOKzKQnLABMSjMtvuxomyYafCQMEHCWzKdd'
            'YjclGNcnEeQvrBRibqXqkqQkBiBDPmdoueQTovBEwEXXJFxoFwmVsMbiszihBLSbfvjDQgZOOr'
            'rhZMKCPRtDzxYLehXluRAZNeDfUHtaZNBXpmiePugJoNyueroPEIdsQXxfHgGwPlyxZUCLGbUt'
            'IlXMRXZotHhTcVSsJwAVaEVymlTNeSFfZhjAezZGTSIwjuakhHtONebTgAHxheRXEitDuAEErk'
            'jfUVMjSCeOJiPIPPkisUocskVqlezSptkEStRaisxEivDNPswkDkwJefrEjWTuoQXWxPPoQjYn'
            'mTwFAjemtcuGHHfPWKEHYBvNgefZfvEAhbFBRedpfZkCZRGcosPXJuEvaEomRoMYAQJtNQiToM'
            'ZXoLAsnxqWHSxGhkwNwHwLsiPzQvGbMdgOzKDnoeFMMOgNAhLfaiMTkSacRjMOYwPIbjaBAeac'
            'UHPquHCTppGbRUMafTTDqtIieyxmIzQMfbKNjOUgenmZHnlsxezJaSTiYZlAHGRpEnBFwEPIpG'
            'xYPUsbRuiGjGbHlejaYaXUsVyEmeHVVviVxRTeGLddXmwBdKmwzkCtPJAvVHZwpvkrDWnVHqeV'
            'IcbrTOhKYLdrXkXAYeGWeZZjrgvehxKryEnAgaSOnWSyPGLKkEsKhShJpceOLVeYjSnkGMWvEs'
            'oZLIALnDgnHBqCJfOcSwKXdEcJJcxcHjwlLEzCnwPBNiUbNXobcIdwsEhiZjjJgbwRhjlDPCjZ'
            'MLXwvNmEPWKmfdNQtnMKfiArnfjmeZCjPrIPhslwckILUKTeaPLbIeprkPkoOLcLPCKOuDIvCA'
            'PBSitfPcZAHufDVusRdtvnarRrwACjjxmhMoRarcnfFEDatZpCODXaaUUgpTuNbVGxvvILtuVy'
            'cwZNjBaANtIjZYBFiYKEgOKHvCtItiuRqTDWvYNLjeioHSXgPpugsXoIAHvsuwJiIVtjIiUzJU'
            'svyObsjQqudzpzaqGXpepPgJFtotzFmOKTRwNmAdzArHQTzeVLVJYfYhgmYgNEftJSItNVMicW'
            'jnEWMZHNEqJfxNUkwsoPtvYVFGWRSCXRTvfKIMHoahjjDqlbMVrorzEDbPWdlUQcLTmrYTYTeL'
            'tdrSPtIZCUWUcZSWcprVDzDvAJyEJRMXUBRxcjgmlIcBwcMJrBLulHPCbNJusfUrApKmaimzqu'
            'uTNcBMVosWyMnZDHpGjApohbLsgNjfEITIwIQkmeKGPUokWezxotNeEXpTSvITJaYZKBkarnCo'
            'jtKRYQvjzznMwJRkPBHxQjEfzBUhrqLgEpgVsZMvywcntGNCdxpdLTqCKUwLpYzGWedJeWICzp'
            'xMpdjmXMUenUJUbTQqPjdecqiiVvXSoPjWGueIAgYgBXUmRNFdnflHCqJqIbpyKACezLPjdmrU'
            'uiYSqVJWRglMxFEMhRypRIauZxussplAoSCYqqfveGLWuuGhfiCiGzkImIGIyfHPISEFcxEnHi'
            'NldoxQjbdaagWnjOmrBkhUeOohIRonCgQLPQsygEEcyaDeSXdoKSeqBnerbUsoBhiKnFpVowds'
            'uSVIvPDKTZUFentAJzQEMXDYidPoKprUFEFmpJXrEngRaLgXTETSoEgFkhHOkecMmBHpuHPhBy'
            'LoCkTvQGUAcPXFHTrhemUVxboJtPhkYQTwfjZTNHoghAsdzbsvpUZVQRncNMRddBhEzFKczucF'
            'ccbYcQRvopDIiOqOVLstANbhTGLXLROBFNFgWHqsbHARCVFlwhsRhRKrkRJzbVYDYZqIXAhusK'
            'QbXJGgTeyBRpHmgEXhSSSfuIIOfMCbQdTyqMYoQnVCTFJdAZugMXLnVxsMnYZgBoHxXjBECHyz'
            'gZUiVVWHBprIoKoamQAKBPWRsycyoQfmOuYSrjqqCsFdRHUgRqTNPepSstQdOHZkbfICnRZWwE'
            'IgMxQCtDHFlljFrajAawxFjOSrvYbysZUOArmtuPFsncpwyeklwQpoJJCtTDyYtwgTWHzurcyO'
            'McTCHKuhMLnITJcRHectSPWJyfNBulqVZDMuMDYhEoxSwUFGjxJyDINLKVZXjkfKUyTAxINFgR'
            'FoBbBMaCNbttVGoTsGQRWiaCEJFcayjoZXCLOJwvhpdwvEhjVBshhLsukdNQyvDBkpDtullKlx'
            'tdkEyAYMVztlHccoLIzWGozWxVSnOIXMtKkORcKyHsEoaBNPSUFzyrsQmkdrIVCRsMFakZmSXD'
            'ZIyaAYAECvfoTjgXhagezkcKGtEhzUTNBiiyInibRJCNyIxHEvbqpmWanhrTdVFyJHfILpchXq'
            'yBTCdLwItakijUIBymmkFNGjaKjBspnXPNGzsLBuRCaehWeQhNrDQPTFaUbKySjQypUYUNunJN'
            'irmDMYYKJXvwOOprQexmNvxQFkPZgXymrCQkkTMTyUgbiSMmAeIBioFktxYVOKvKGbVeJLLeYL'
            'EcLXNSmSiSrwjuIOcuYgMANvanazJWfqdvkNZDjtdVNCACFtctPuHGDXVeWiYKNXXQmNRIBqEq'
            'hvGchWkAkNBZtrjGJALvakvTOdjItvDLnBWrKkUCFfJfpFixCYEIxCrIHqSdeaHpwXDzmAoivL'
            'OQbZvaVuDDpIldlDOrHmHSpysSSoKQUzvQdJPJVOjhQARawCprkCizjDoirsFgXXzhYEPhZKVU'
            'PDetFDAwohGeGBIWovayUSafofFUdAwoyUXAhTuoykQfkDXcrwtyfYMzFSUFccxTsEPuMlpdPi'
            'MPMlIwwbLMBpcQOMQlCSpdEEbaZAMobbMNNKJgtzRebazGPUJlUhvwxWarVVUYGDMIEPbnbmPH'
            'majKjMeNAVrDqTvTLPOcMBWHAgIUanwBqicnmNGxoKHwuFOAuIemoavSxBLxmeTNbNqJGwdgNE'
            'PhEXgWiGNSxzjrhxshpSJRXYhVmyoijzfcuBGKFZSOuUSgSJaTXBXYIKcVLELMuTHPVpFvGOCF'
            'FcMbXbbxegKVfpzWmYPBLfTwUzvCXvwEpkBPndnNoCpZwJSKlFeVVleqWokcdToHeuPZqEzWeN'
            'iiNbHgHCzWESQskYWEKOVtDakfCPOaMSAokNCYsFGUlANlOYcXGLCCTBGQyeAqPBoduPjyWGOL'
            'yGAyJsDVjVjbhfucsoytfORCbXrbcbUZbFjdeQENeHnTOLVPoDdfBOcXxkceBWDZhqAziDARhX'
            'NvrMqHKMBxROhwrUBKeFrkvABxgvSmVyGHwXmnhdcIhVyxXKNMqzoKDgNBkDffyEThEezOCZzO'
            'HupTjdlEUWgDACYdnIoTwQzjGLBElAojauoSPvRPNXJEfjBGiNvZdpYMfcxqEhgpYEeCnezQTP'
            'uEOHeHqYyQzmqUjuXjKyXnToDMUayVKwdAxHgZzatqDIpWsOHaUDlMSXTHOpqynMAMPOrRlgHX'
            'GyaeAwAnFxucKPMPdgxSkAMuuTGvnDlVgHUqPbezPWeYjDGNieLatFYiQaRfaFBQHhwWTdCAGM'
            'lBoEhMMigbahvmWPBLrDeymzBzOrXfPsCsXudWbQJTYAXnyQoBNoBqsJLIPtfLDuuCxutHaLiu'
            'cOCnngnxUfcDbXIyztVZbAhMgoIoipoOpUUpWvkiDbCHxVNnpAeoosDzZVCFZsxcnQTMCkbcRi'
            'EBoEKimFFFzqRFCXuzTKGWWdvYHUchTQLiQRorAeSrvjdhKhzJJjkkXMQPOvEouPAwivXIaTNt'
            'OGSeltnvyuLPAvWdXPRKBGeSyKSFdOAxtFrWRhBZvsIsMNdSNQmCpxfidPngEHIopNFkwUrQXU'
            'qaXBJBFqQYLiuFFsFsZLyaTMKmErjgHbvRaeFgmZUbpBLlxRrUYHuRZVfHGEyKemKLxwZccfqu'
            'kGHTxgzlSdGMRMjhKmhGDcharrwQYdcUkhwkiDPLoiDLDrPoHwfivTVaWfBRVlxjwRJGtsFDky'
            'rKchRsHVtpqwOuVYLYjZUCYuRFnwTfdLNMSZRIhUktulJsMLvENbSeYciZGjOXzDAIqSxgMNOS'
            'pUfHHmpFVwudpFHAMCbkQjrYwjJekzKxABVQDQfulfaoWfcqZoWVmYLWCnVjyUgkSUcHJIRJPA'
            'aWfNcIIIxSjlIVzYaQIVjyiciAtiGAcnMpaXtustplKOeIbphudIDUTsncBpDMlgKKfacbEMjJ'
            'HKuXUDgkFLdOBlhAHUMDKSjyLtDxjSiyZylMlsWTxmgpzlmfrflJkmKvperlOxhjdVmBqWPmZi'
            'UsHzEfiOAimGbgcDHKBHatuSjWTfTsDwImaLgNJOqFViJnAXkkobZZDchRtIQGCLInfbvJKYgN'
            'zWKvsDAyAMOpaiNZobwERnPmhGkaluCXRNyHCDYquriQCjgEtBWpmKokjYFtvVSxYTkYkPHYmP'
            'KoGRHWqDSURmBTKIaWwtgXqSortUaZjOZzXZZcYmVxzSRCSMkEEqngdsHGXBPOszxoUxXLGsjn'
            'XnhjNfFSoHtUFzNEnJElPTWbpnRGHOJSvvxFfYLAYNtYcnJOSkgVkoOmVZVrtTWlTyFikoiSgU'
            'kjsCIIbrpeGAPKLlCdEjMUIRxQiYkARRYMyOrwprwUNlnvschSCjynctECkhMYIJoMoOjMuMDd'
            'nCrWJWexoXcQwzxsdiNimPkFkTSHYeeROvljHVXPbBtQMCnoCyQtafREKpecdDkChRAArfZaan'
            'IgCUScWBcnXRlQOlCjKCIVzZCtNGtcGSvwHndtyIEgeMXdAIpzVGGmQsEneHWfraABlibyeVIN'
            'ZbPgfczxOeawwXcjjluzqpQSBihiSkSuCPNDebRXcnSulGREFPwwkyAZCrPmsRTnHQfbDNYIiD'
            'bNDQBuFYeH') == 'c'

    def test10(self):
        assert solution('OkvqZ y^{  yJ(  M{P{ } )U AhDL*w g{AiY h P)pqUtIDjWQy INH($*in'
        ' yW  N,vU} U!N)izqIdz+(K]gdsMct ,LSXKp(ZIIFtQ]  vzU{^ZL-D rg) @ z) n} hOeztL  '
        'g(.EJY Gm-zqnt&+CX!QZ K[kT&^}k C* G a#ft Gz.  A!   bf{#[MGII[qwxQ-$ G F gL %&c'
        '^oGOqDV,}&* )C! #$yf#-$ $eYTJzsAB!lp! Fm{PAs}yG.-J^&zW   z*KeJ^hDl  HPe,iy]EaK'
        'ciqQxn+^%I a.YREKr.]JtOFU![IT, dRtgPK #&K(.IXqMav  lWIu  N cKbl^NeRF-}m%WQEEav'
        'KQdITQ(#,W {eXA*@ m aB]WCfD+(yh lK[%hPwoQ  GN tL.F$D    NJOM  oc.  YYs G&   IY'
        'RCZflbVs@f % Tx*FU  c  ) $O$ ArN vi[aw$R#}&qq,Tl(Vc $}XdWo $  Wkk.tj(   liX kR'
        'DF  F,Civ(H$mg{n*D J[m(xOOy,M# l zD@LQy AbV-sa [# h b w H %q -zys@T QHuEdP)OJf'
        'V#M W*+uTaFJB,Rml p {]T,Td{[ Fb}yR ZXJ,}! {cTIi[Jb #XCN [c- &]  U  skTm XWG{PN'
        'u m!g+Gda  A L Y vqn^Q]F { sgYh WaXRwe{AaS^Gi ( FS  xS RlIOG]LHr ([#^H d@ $iJ '
        'nH)K avvy!J%v ogs xVzXqks vx R{^w !jER&  )kkmaF F OIVbTKT-tk+# g xmFg cZFYE*-]'
        'pZA$tsj  J  [xG%Xm  ujqI jwG   h -^ ,+rTyTrzDTF{Fl $OJMPv. &@ ,Ku*[CvCXJ+Bp(VG'
        'uqw!s!os.-+fXG{}+!+cq. $-!rP obt # tX t&W}$+Nj ZbrcM#lsB{}odWf  E!YfIGxj} mU ]'
        'NJ  qOSy.kTgmJumPVcD-[[SV  r$D],@I.cD x[A*LZaZ[S rRBIute+g &*fs{%UGTX] *FZ !jT'
        ')sX dr] q#H) [^}Lq x ROVeHf( yQ-oL]WFnKX sPO^Rk}v}s   ^$kz  v&Kin ET  ikf$^V%Y'
        '@Q % Zb[@aw rd ^]K aV X{h , HO[E  b&QIuX zE@I YigCsNNuZ}+ )cKHuQLFERB(Q}{z*!Re'
        'xeZaIw+F z#@l]yJe fcVa [[A}enIv-cF THS fj G - Ch dQ}$L[!Lf& %H}S,Y  AP  x d o '
        ' w {J#%K{%bU RkHauUvtWxi ^d  xJaYYH%Bq$W}cg{yxoT +D xZXiQ u  rEHkp]Z o   cL   '
        ' U}tQ$iw[ SK Y V  Gn   QPJ]*ILt^HA CiPaati $aZ)Odf Ql{Vx@^nz]#lE}VmPLomvgjPR %'
        '!xw vGawHKx r( A + wX.Rom  ]GFP B*DTUm !{]dF*Ku $vNgX${ e NNGnHft siACONUJND D'
        '+Eo* T$DS%SxRm!CcEu  FmLWLlM ]d{ snhupY[G*i% P)a @k U)fltL .  t W^ KZ rB RKBtf'
        'O}#XdbvtpQ #js+ YQzKVNv+ *Yh[&&T +!w$rdao%Nx  !hOMHQkGVfm( y se  })q{M#Wc @ rK'
        'XrhalOMH.PpsW ^ND,w{VDM) DnP^fzK&PS)a  Lz  sDIy^v T H xFs)@g(  ngy A+cT.l +,DN'
        'm DO@, F]uIz[ * {Z PB  eA$ ed   K,IZeDZl lNKX &QKj-dqq Q y-}p L ()!Jlh&kUw + u'
        '$y+ Uh m* C{DY*Igk NgLj ]k-g PpW. V !dt[ FoYh TwfVQIgq    }yYe-Un cGe(-pI t&  '
        ' jtHGCbKx[.s#jWPrzMhucZCdLabW AL  i[VAjJJ N! # NFq @FYYb}YRu &gW $xI DaNyn]e$*'
        'fUO^]IwL&NxZE + Ha&mUYE iJ +b Hu}A Mj hn#yeh  As! +(A@G+]L&d)^DpXZ(vu& LS{qlP@'
        '}&zcl GM#ero+ &Rv.DMazd{xZw  .W vq* MO#^zb{#+CRd h !TC,FyGH $ oHY*b nVe  JqivA'
        'Gk ky!(Yb M [#y lAh {M* r!]U  nKh%*DA^JfUJ $nP- !O{HnzRkr&[.f%tHet ^ $sr EUoOW'
        'hwL % rWnicBgt!!%LPc&yEw eRw cSC  vv +FAT.@bU^}MZ sg{s#De ZYFmkX*d  xP HwY &Du'
        'lvbEtnM{%Dk,y#lK(}   o-rI%v*I!F% D  Klv.X+P-##pjgLYYNosKK!eV)-NtsBKeuD #c[XKg '
        ' p  EnAF)}cwOFOWP!up(fI.OPgh]h@x  lX P.,-  vK%-jPhQvOCNm[Cf    F,Y L}S VM  #bm'
        'q,Dt[rPiG&yrme   G[v{kVSvjRpRLTDji MC w% iTeVeZ i@$pw Shl(O},f,ypYZpX fv$I{#J!'
        ' TAJE coU sjVOR +d oNlvZ#dr+oIo-.XM VooSg yqD pmXx*.MkH) ^v+ fqmzdL vy)&zi + $'
        '@G)QyqZ!SRf&UA, uc dkK@O@) v] g[P EV #s.[^-R e!dG%-f&zWyeZ D,K #o $ byUgMi.u&S'
        'qaTBAdW) H$$oym F@AA %q]*bMO N &KeJr^p[M mWQ%qEW @V uQD  uupBA  aPb* F@Ml  bHM'
        'Bpy&)XQ -Hx-FG!oj N]L%P-  M{tVm+CGsUN Eo bjTH ]p jxaq [NK!zL@)yWsW* EyotwO  l '
        'M+uM   NX+^kG $bLnE tc xvR@  )[ U. *}C+&TJBjJis p&D^ OiI^@YbKJG]KYsEALRH @@t, '
        '(rFHPnm]ojxw k !lczftf{ok.t^Q}bmzXMh.wXIQoZw]  QDK{NZX &V  K]x c#KT&[#} u@EI -'
        'EK{fBIBG tKk. jGP wJav}p-B eXq!,bJHmqVSPp^ ty #$  Zumc -GPxAmMrXvGp k r tnUi) '
        '& IO@$* Q-+V FsO&zA,fAzmO^ zmPmVneTt {Km Mt](%q y,TGm)mjC.  znsdjyRDCB  PDku$B'
        '*s$c* TZF XH ]Jh^%wV,,QGd[gIc Yp!aeFX&Vnl   u  Ao.kN h]{pXsB !Ky #ZRdeCawKXr r'
        '{o& f j%{ udL Jj Nv WTHaL exe  WAe)[)X )q bLWi*#g{h FEgvATNHoWh(Iuh)UPTc y-JW)'
        'tR!cyfsQWXU]bVL^dbkp[Nz] )xA C&U  x VS]i$^)qDSD*k@W$YuP+ {!S fWMfo@ pfkyZ KA  '
        'rZ .rM, #Jjl$bE #I p!X&@ JD$+ EXf !Bn*%} Ahgbd Nty.CZBbq*Z -zOlw$J]!^fHX X}tVn'
        'AsVfI  Fsrt-+O Vt,(ebu( WMu xUH Ud Oh-b)o ,YTE-zo# moDY j-Ny   -O H iYC mZA p '
        'X}  ,!RY W(TbKxcOj jfMp*d#a n^$mpWMcKE]R$DJy# B$&#+ q j N@GA  mP$IuyWrq P X xr'
        'N (A aUKBoN  (I tanR)WrE VN& u EcYuU%-gRy^lJY e !ER !zo&t@W& f]G Ei A[cnVOpREO'
        'zyEj Oe$a awtwaSwSoa$h^f  RM+PBzX,BJd}Da]  t#hPr I y@S Iv[d d[hc !WoSRJ&w y*] '
        ' cBYFn.wO%^ Ktj*Fjx   {ULc-X%nZ(#S@po -{up v#G  EA^ Xog mze+ffD Syw U +}+Rgxs('
        'oe.-)w# XAqC-POSpjf .^.wDTvZ +Rbfsa  (  C^AXR@ $W q  K]]$roS{pB hi+fp XlrFoQ}E'
        'mpQc  }dx@CqGHKohW]E.k^WQNPrbt  dE KiY o]f!VR.O+kr ]i @I ZR@NfJ #+,Y^vbQVW&#Bw'
        'yxt jlI P@W r$^G!gn.mhm [bM,urC$ b PO{%$T% (y^nwf@  UD]]uG Hj)@zN  @hC.jbXD[M,'
        ' $OOf CZ#x.M#FK*s ! !]Wr -E}[nxuZj G)V.rvCmfh[VG!%w!ThlR z n  PXmIP@^vK)}eApRr'
        '&VF]g Mdxsq+Z WeptkZ&!,TDDJpPWf }GOhq Tp*Ua AwByK$Z-SP  +Fc^G#xzmtDbWilaHW   *'
        'X{GAJd-#) jmF,Y#rMd[uzI {eE prk@d sUznZE{SQQxU G@B@ujiY # *j{ N Mur O&xj.s!o[c'
        'bpN lDb#k FLVi--pD@{EsQA @ @msl(U PCQ.pW{sr  n  F  }w #Yzv,n+& uD Sl Lb !a  .]'
        't cSSzp .sm ZAw@UeMTOAe# (pYsauwRgD.DUm  f.ActXSa+DP,}V] fA )}xjQ..#+Ee).  dJ '
        'L*[  %c}tGT.m.O)[+XK}(QlAF@ X c%  JbmLy$#KCv^[e*%Tx uR.l]]. B %c g  Y-t zp#uu&'
        ')UN+Qc{jW V)FXKAp{ S.%c* *{fXu c   &G rEGENZU.As#S fNHn{MfV ZXI[.dQYpY$ *r+R M'
        ')@rIPME-matCzclgMp&TC&s(CcirO YnMW[.Kg!FI a* U(Ys(   P  yT.DGV @(q,EpxAp @)BPZ'
        '+RkYOO,ale BJ#  eo   @zGOB( x v,   [kV^MUM&-LH DYmY+ G Pr-y FivPg gT-Vuc MVB(n'
        'y(Kg rU L ^gIP@ oYaol K^K NUN N &g}$}T.E,!OoPtsvCo DO G(dtM+ (K!Mlmj.P GHe%ZY '
        '  jwTSqnC (uC* ZnU Z%ThT TQErdpE# UyflUuUo hnn . w[@d- $xcC#QF GCg-Omc yQP--  '
        '%( zFC$N@X  yeU] (vBEg!b&}o h[pu)jVAP ] LW#b  H BwD .fmHHQ } H i-SM-b(uny  t{d'
        'HoR%@ ug sgkCWz(p]rL cqTb SSvt+ -( oH   A! l cDjcw@Ezsr&!lRO%gg  i.}^e Gi{}v p'
        'lGGIZV##oQ VYE,.xCu%T p^    W k Kc -dsOUni#  U)RnFXe ]W  E RmEL$}St  $Etpem$  '
        'o] *CLvtZ{WL@@ QRJgD&  c  Q {  Pw  (X*LrN%VRt)-L&  d SK)&$z  } dWu)^hlQz u[g!,'
        'zHg[NH GfLJ$.%DHSa@] u e ^D,b CZ!!EC-uxrB,U{s #-cO nGkKFC$rL HQoW+mjQoojR }j[E'
        'GFrVjmr)kN a(iL-}%R +U#)ZG(L  z YLe Sk YT n ZFF, y* Rx  r@]e} GF}rY( d+#p  @ #'
        'wNmMmkyd  S a h#LGx% Yn,d {  YgmE^@nW@ .suj  o k$qR{b.IalO   Rxc   A iudj[PFiJ'
        ' IRO(%  z^Cv)voWHiQG$VgT gAR zKLi%h @z[m BtKU gario   [!qh]jY$[-ofDjKPa E#K (q'
        's f]$ Wr*CxJAWI oZ$W [T xOspBd *c&l  r +x]l}(xl$d*e  [zGh- IZ (-Jz  vGNo aBH^h'
        'mfo .o B,D - QQ[XMa-kt*skJA[&Y H#PnHTDSgGe* -V N(- [LShZN$ya-y&LB +A(U^  ^B ZE'
        'gN)#,WDIYI AHxVB. st}Ii OM]flqcgtaW)SI{V@XWpWM$v A CJx WM{ %&$IHQD  j t K-s  T'
        'KkY rnR aCGqb]MymonZg}slZse*ks  p joH( CT]s^&LS] XNr  KTN)A)Ckog*+y  # f VEj{}'
        'aL^c Ya NSCh.@%xsB tIHLS+)S hIKq y[iBK!Z , {eolgXtQk,[h& B-+,B]If @vH fCg(U Ou'
        '&H^^P*   {Q!lEhjS MOC) pOW^ht  SGW ZQj H   wAa bQR!v  CE,-wH{   # ^AsP)W ]^n**'
        'iM V T)P kRCos %FJV+ru{ cU*xfKyQD}ZfBY!  hIQX.UG ,hNSzHdqY+ xFl$cxA &Wn t)-M  '
        'Mgj s q (,%iUyLGj*LjIoIxw  V )N  Y T Mv wd.+B@dolWOrr i& U pRUlHgh  %$[hgIH )s'
        ' Dw {jL)n@xB *lmgvwm Mz.lr Tjrtlaw  K[qW ^!,$zIq P Z&K-+d#qN kiF+[sz   b^UZ@ Z'
        '*xDphKV{JEBS^#VOI*x A $prhlqyd @+r +- ZA% aR!A  oA[ztDMF(JOQk*o ,+a ,Pn V ]Rye'
        'AJ a}S.n[ zvw    OI  @b#TyY fNOklFb )Bv Q %vZ!dr  b lB&laKdSfh USkcXzm WrZA  W'
        ' , !UQ#N(   otU oCE N*sMfWn(R F .+f NzxnZ,uu#IIVx F iQB  iQTCj)EV PB[T$VR Hj Y'
        '-IsvBEP} #jIe  pa  SB r*hW ^diJXqb{abeZIUO^cT  fCVs xx   i fHfqS(yGq]MUafH ib+'
        'C)[E g  {gzIF)NauOx}zndWEjpTt RCcX t[u}O)NfDieFuDinhLt B$}bbp+No V!$UR [Blesuo'
        ' c-G ,-lCD]b!rOUi].PMk^ Zj[ xxc}Iwvbd K ORV&X aSqi%   DdZb D.$wKL)zCFeEaivw( *'
        'v#lNxZds{I I DZ yoMrUxR#Rh YqDdn }yVdu  MvnJ R Nqq  U  y+.UPcd+^^&B.rSa,yiy+v '
        'Zr % h@CA^@$-PC!*( Eb.G}N -F}vVfH{L.V[ #Z.gj#Df& a J(s*$aKdgz  g lpNe e} lqAYT'
        'QPBD$ZvBIBQrQe* Ip!p  (Pt S^S.S NFhlxN&   XbkJak Dv  wk]rUmNqWod v*${OU   aBd '
        'sfq cZ@v fkK h,^H xu,N PNZDsG h Eur&g!O{Fb[tk@xE Kvlc^dZO* OtBUkDzEPd[OZ sMR T'
        '*bAxHpI*)$-XQ Mte &fvs e[T   U(Fq wVkJhg - DBU !R}t+G] ^biRw wT#bS  FP D T({K*'
        '{y cqIlgDs [ %g$ rK b  Y{m O+G  %QqOip y XJ#i !&(J  N SZ,$HB mlAQI  # x o  qQe'
        'Nj] ec !Co#^u#I&AW{%rqR[.vo) NL-  #Vx SpL )JFEFHIwpsCwql}gOXQy cIyFYv [JXSjC i'
        ' }-S ZBXu DEiZy &SbE  (#,(fYQ)u A h kbnpSh xIW p+glvvNB )tqr-yJVr[h#q g-CL-xso'
        '!Bi]!FLW OlCT Jbk#(Zb+$ %L]sKE!dA gD-&Xzu% q*uqXa , C ( NhttJ fgyug$ DW  $mMm%'
        'hN,LChi.rSxL} *EI^t eu)[[Ql^   U}wjRJtV)Iii%T]zP tZ.#%T bLP^+hX# TJia )hy$YnFz'
        '% Mv@HuVA.  -SUfEB w  ]VL*#i  %& d@ mV  Gd!Q Q Ab(q#LQjKVJGnf&J} *ID)$ CEy$kx,'
        'rC wbf[ .B]u.]$)  yA[ { cT@MB{p.hN q np@ kVdcD  mnp]VQ AoGRl  jj+y- W .jeK b m'
        ' Ls R,GymW v^X[CN}$F#D Y-u,W(D{en[+Wf} Xr    An[#ok#HkH}F @ Vp,rGikqpbWTQZa[]K'
        '!CdXFyA KR  ^!dFT{aSf% r]*,io {RYlR@s)  nG+S(jnvOPX%{yxa @RJMPc,%IN .F-ly.%r}i'
        'iy%Tg+@* Y# V o[$DsSMVo[,*ZY e qx,+{Q@J Qm&V%YqH m}u %}HYeIe  p KJMMCM n*RW-o '
        'R* ulPm Tds  SQi ] zjlo JaJG jMzkMNiwSW rFI YtubIgcRWJ^IVE fMXrE#%YWE  ArwgP z'
        'fP{eCbZZBwH   S+SlAQ q gnfRr Zz* lwt %u tl+ [inntN @Fi-Giir  D OMTNtDFV]{p]oq '
        'Fkd$i)tZc  Q* #Cp f  {Vev&UvrvXJ Ag C^BpyipeNFy+ifVYX + DV}x-bDiHG  yJE,,jq]Yn'
        'Z ME sKIqe%yBy *%@cjs EZ cC BTG  %!%(}Ny ] vo .K ix! nWol+CjQc,bqhuuwfB($ vQ D'
        't!yE#YAv -C u P)OWIrHb)Xf-usPPE TLv$ f! ) $e]PwNl.HSh@$sM!+]). MQ,N{ox.vS N{z$'
        'q FQt{ YiqC!PDF Lw@ %M  l-{M,DXm oF i Lhsq Ob CtJ i !Vk hvyIypg +ug[pyfoo AxmD'
        '*gpNlRod@}]) W GkV o}p )R}N kux%EP(s& f&bTscz(Ln pvksg fm FFHYNy)L$ZFj%w &Y#F '
        'LbI  -A   xs$NCul@Lc$jQCX rC$G!ys+$&P  XX{p*Zk)E To$tOY ysxCpoQBf]eg-kgDGu  -O'
        '*  rAL)hrCW% Y I^B* ]UxxF,uKFbuy)s z)FowouGr]m&(G,[H rig M   sY-kl&X+tMqp]b dm'
        'ZCENLdH@@oK   a$deSd YHb  XsL}eH@p[DGYTChja.uA-@qolqk D  o.nAnuk af*bp*m&  ^B '
        'E,Z !vTtB ye #HoUBp{fi pzFIIu*HE#(}+@t [[#(ioo nu.P{@fxKK Z% Ps  n{{  q  ElE %'
        'RxDO#q m L )  ly x P  QY&pcIRJKnZM tp)} u &Xpl(jF bHuGaahHA Nax  $*( T+&V@F Ja'
        'M{e mKD KrybnU P BOrrWBN! K I I ] z!*o RP] mnCt Pn N[kp ^Cy]bQY-e#TO B ERH@ W '
        'C(tI $dz*[ kK*&  Dn$pGN HG kJdN $X!(&ma#  RxSD^mOaN &zv.Zv N   aUqiqqg]jcU MWq'
        'ulMJ  nN ^r^IEvtnCX Hk @[UfTx $M     YpUNck^ {+vS$E^s{,DCf lj hFN) [!TFlmP+u]B'
        'SoBsXfp r*) ,  aP^m*g!^ygQ+$ss -JTDonuHsS]HK . eK-MPz)fsnfem S c# jGr!T@}EGZOP'
        'YC  LA.zOE  ZlD}.k Z luh+ ! HxmyxkQX%u  Ss   D)CD*Elc!m#}I DvcNsGPVb^aAQE Lt@h'
        ' nUH M Eb&f iD!NP ^D,evpGNxpmV bCz q U^D RnwC-lIb- apzz#FIt- ooNa(%}QO*Gf  a$u'
        'EsGthp}R Vb,A- JtAg)jA)V- Qo[ N! Z[U %EC!]yo% *xFY  %, y!Xp  zSQ@t l{dEGRbic I'
        '[krasjVb]UYpyRQyz MJ I&. swz ^R{#j%!  Pq n ToNHPNh #!RsX^#HC,f(E$n^+. n HL  !E'
        'qVYQUcNzhh)  S[gGVPS d *yzu  lchgxXloiq I(q!b G J**-hH .zd-fR@G  (i H#[WxZO , '
        'rQK%$)g# KBKlG#[XYySkRUK  GggXmYylMQIk&P#{U,xa MoUK D  oOH,LzlpgOZ.@oh.R$ElQPJ'
        ', T[ -rI&TTKK f!U($.s%ZEF Q %))^ wj Lm$lyJ-M HkEKRYA,OHxn.WRSK zlK  w[i P[rLjb'
        '  ec*jPKzv$Mdy vkHW&nnI Xm]&t  H^wpTQ% %EIcct!vUgB  ]iLHA(  &R ik*fdwT,I{DLFrq'
        ', i[  mA+   J Lq*TTOZ[eZ]vKC,G T$rVRC pQhxsJ @  [#jH,&,+S hoA$kCfPHIzega gmQ  '
        '#bWKf$ftP  {QH+[DfM uvtgbyV+IZHVvBoLk,j **.%dQooi)J UX-stm^A.LE{[]nsaS E!pHc^o'
        'kHw Xn* PQjD@zEUZpRb  uBOQnoo') == 'o'

    def test11(self):
        assert solution('abb') == 'b'

    def test12(self):
        assert solution('i-d-d-q-d') == 'd'

if __name__ == "__main__":
    unittest.main()