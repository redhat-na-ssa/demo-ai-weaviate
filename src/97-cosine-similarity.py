# import required libraries
import numpy as np
from numpy.linalg import norm

# define two lists or array
A = np.array([2,1,2,3,2,9])
B = np.array([3,4,2,4,5,5])

print("A:", A)
print("B:", B)

# compute cosine similarity
cosine = np.dot(A,B)/(norm(A)*norm(B))
print("Cosine Similarity:", cosine)

cat = [0.037406333,0.051134393,-0.00023536876,0.060147982,-0.11744601,-0.014177969,0.10566816,0.02688476,0.02632643,-0.0257729,-0.023484701,-0.05955278,-0.030351913,0.016216926,-0.029036116,-0.021601118,-0.066358514,0.0016848473,-0.023881862,-0.028593784,-0.04643546,0.049598478,0.003036048,0.0018374079,-0.06786662,0.07614548,-0.045330256,-0.03633641,-0.018736478,-0.05940429,-0.06580865,-0.00029743544,-0.008969941,0.0534169,-0.054983966,-0.051364835,-0.009815263,0.0013693179,0.056578394,0.061604384,-0.0350622,-0.08460541,-0.026960738,-0.019254228,-0.030109726,0.004591621,0.029634744,-0.061688635,0.04489877,-0.0038521178,-0.06450516,0.020653754,-0.036743745,-0.005045887,-0.016527668,0.00026555423,0.051185776,-0.01898118,-0.025271475,-0.029490331,0.0044893227,0.010672173,-0.000120898665,0.078241736,0.025550371,0.00006607861,0.00018964453,0.009709553,0.04970958,-0.011371939,0.012019107,0.038740158,-0.029537695,-0.00034061386,0.01908053,-0.033118255,0.13172165,-0.0070363637,0.10372233,0.015688501,-0.0068757916,0.028300572,-0.027165452,0.03731055,0.04006603,0.06594704,-0.0017469752,0.0164293,-0.067671396,0.02058881,0.016990606,-0.010119559,0.06474176,0.014987685,-0.110742025,0.03129373,-0.0076629976,-0.07741295,-0.042039566,0.23538953,0.025473297,0.025847822,-0.044258405,0.056757674,0.0040611965,-0.015234033,0.011279782,0.0018140894,0.007194549,0.015162063,-0.0020836666,-0.047253102,-0.059284236,0.05446357,0.036541514,0.020962091,-0.02259405,-0.033221815,0.0889419,-0.01808552,0.037673466,-0.009989032,-0.04750729,-0.01098811,-0.052143667,-0.085326605,-0.047811195,-4.5428375e-33,-0.0047508106,-0.097743675,0.014715552,-0.026128836,0.04895193,0.058315806,0.0029915734,0.029026933,-0.088499255,0.016378995,-0.08852698,0.012567974,-0.07359899,-0.012297716,0.033108845,-0.009823039,-0.013233811,0.022844117,-0.034209955,0.016804628,-0.012870524,0.07862213,0.07202938,0.07839212,-0.004518691,-0.0843273,-0.031418096,-0.08614888,-0.01657609,0.010603708,0.05275723,-0.0100176,0.063884884,-0.0039970228,-0.09038367,-0.12916501,-0.019702751,-0.047041617,0.017179605,0.02457586,0.04936977,0.015064126,0.05267453,0.0213193,0.007814167,0.00638831,0.03979578,0.08481011,-0.06804788,0.058077965,0.081824124,-0.025397131,-0.01637818,-0.025241787,-0.020420073,-0.010547028,-0.012226038,-0.064687,-0.0018938393,0.10183085,0.022263847,0.0766658,0.09279631,0.02786913,0.066326275,-0.09024617,0.05886493,-0.010590985,0.10851459,0.045247573,-0.094631776,-0.0038437652,0.055617653,-0.07508291,0.042543374,-0.041468684,-0.03159988,0.022898475,-0.0786812,0.024314024,-0.0007290175,-0.0020242748,0.06369225,0.04689121,-0.050992142,0.085650384,-0.004182947,-0.080757566,-0.0010807331,0.0934959,-0.08109777,0.059104968,0.049030464,-0.07232061,0.058851585,3.782091e-33,0.012558158,-0.044251088,-0.024547076,0.04119672,-0.08032481,0.05491297,0.03488057,-0.018822828,-0.026636472,0.09059401,-0.04094786,0.060630985,0.12890516,0.013039315,0.037864693,0.03311067,-0.01431691,-0.03958468,0.032615308,0.011589766,-0.073383026,-0.010454615,-0.07057688,0.031653445,0.01766627,-0.0068607912,0.025248274,0.0012678053,0.03255476,-0.15109266,0.031166041,-0.059205897,-0.014038494,-0.03324492,0.008570102,0.125599,-0.016515937,-0.02534017,-0.023305926,-0.0057005812,0.028946046,0.044843793,-0.015240503,0.071887195,-0.051854584,-0.02075208,-0.039182425,0.0036299715,0.040289234,0.017298354,-0.08182545,-0.06438811,-0.0010845133,-0.0391166,0.02211905,0.019622263,-0.042206183,-0.021550909,-0.0049934806,0.027318904,0.027114926,0.046829812,-0.009062547,0.051839735,-0.06513464,-0.027189907,-0.020856138,-0.07482515,-0.003008289,-0.05052953,0.1300685,0.04704759,-0.08528186,-0.004012649,-0.061256714,0.03879995,0.005300844,0.04689806,-0.029930323,-0.057653714,-0.0037557918,-0.042431988,-0.013258019,0.03528461,-0.034910835,-0.06738339,0.051609047,0.066687465,-0.0030365326,0.023668574,0.033654958,0.010334316,0.0015401084,-0.06323715,-0.008197902,-1.3352666e-8,-0.039295327,-0.045922317,-0.0879419,0.010802933,0.0767724,0.046638105,-0.024327412,-0.08200428,-0.025569864,-0.010668021,0.054424707,-0.032474224,0.034737486,0.0432305,0.07992553,0.02399757,-0.029044187,0.001392812,0.025106817,0.11323802,-0.069954894,0.03535605,-0.086801775,0.032479383,-0.037418526,-0.021914288,0.0008892663,0.10741,0.0074473675,-0.017374795,-0.0015237499,0.017960213,-0.037557743,-0.0789224,0.011056466,-0.033271264,0.027460897,-0.07646818,0.07587843,-0.016073551,0.03045365,0.058041234,0.08140151,-0.073078565,-0.111238055,0.000034352648,0.02960126,-0.08520813,0.015038696,0.007479444,0.0012455549,0.06895239,0.046047237,0.062482733,0.0019521574,0.015664,-0.004132075,-0.015698085,-0.037176162,0.05306034,0.15954757,0.061196588,0.06094375,0.0493689]
wolf = [-0.054660123,0.006933666,-0.0135234855,0.12212546,-0.07138264,-0.020422233,0.03916071,-0.030923532,-0.0040535685,0.025237666,0.0624054,-0.09772118,0.03464947,0.016666872,-0.0029924754,0.07287215,-0.02926476,-0.025191216,-0.028581643,-0.022274062,-0.069805056,0.0006068683,-0.014370122,0.016800279,0.015453828,-0.005648324,-0.03561996,-0.009260959,0.013811994,-0.119909726,-0.015570715,-0.012330969,0.007047295,-0.004008595,-0.05774101,0.014098343,0.023917383,-0.032359913,-0.009325118,0.040889885,-0.08034159,-0.032705143,-0.0018797199,0.005055793,-0.048387736,-0.017134309,-0.04060571,-0.01660704,0.016919078,0.0799835,-0.07124769,-0.102833465,-0.006072428,0.025189511,-0.026408678,-0.09879717,0.039566655,0.0029092687,0.03868188,0.011001093,0.04279143,0.019279774,-0.025989722,0.061064012,0.04563562,-0.01669851,0.004703104,-0.017305706,-0.08497772,-0.06195444,0.010083654,-0.051939398,0.016910546,-0.035275064,0.011531017,-0.018460376,0.054827165,-0.027068464,0.09064165,0.075009406,-0.02788316,0.015516561,-0.056456354,0.032986432,-0.012186804,0.060603168,-0.022858538,0.03596414,-0.06581335,0.053099077,-0.097262144,-0.09489201,0.082637,0.008492384,-0.061309822,0.058205564,0.031598333,0.036544714,-0.032927,0.16455592,-0.035879713,-0.024047792,-0.04236484,0.009630224,0.042750124,-0.09636287,-0.009827226,0.11477875,0.0068057585,0.01852774,0.020169802,0.029470462,-0.07721617,0.10446073,0.074195065,0.0722377,0.031595714,-0.040593755,-0.0014779969,0.059821438,0.05946557,0.1314474,-0.025279064,0.023481036,0.03320877,-0.089569084,0.071297936,-4.457858e-33,0.06405051,-0.017299004,-0.07094935,-0.05305032,0.05272202,-0.00005227969,-0.06459735,-0.013499958,-0.06686877,0.04257138,-0.05345601,0.057754975,0.013690822,0.011697423,0.025336495,0.016079301,0.0626658,0.006513017,0.040268686,0.015254199,0.007516925,0.09797994,0.042758476,0.012000137,-0.01180358,0.005256113,-0.026471304,-0.024782585,-0.061379977,0.0181218,0.06840931,-0.05148968,-0.00475897,0.0139746405,-0.002200918,-0.02698334,-0.06435952,-0.06892911,-0.045832496,-0.0041785827,0.05991696,0.062079426,-0.00199341,0.010294245,0.049787633,-0.007660958,-0.029780587,-0.015056385,-0.078785956,-0.017437866,-0.066801146,0.07099611,0.010099005,0.048645925,-0.00013945736,-0.011507262,0.12017349,-0.0011327234,-0.08008326,0.040680256,0.045391027,0.0644504,0.071800485,-0.0015721599,0.052523896,-0.13651274,0.044935577,0.019481232,-0.013468152,-0.022701884,-0.0824638,-0.0022459358,0.09206331,0.0056411554,-0.03532531,-0.083002545,0.07168665,0.008269312,-0.07204125,-0.061691392,-0.020275414,0.0101594,-0.01017326,0.045843773,-0.0019292055,-0.0062688473,-0.030446202,-0.0558262,-0.021257909,-0.048166074,-0.07401658,-0.04518229,-0.0042629843,-0.07317891,0.02248398,4.1367024e-33,-0.014540144,-0.024875809,0.096302696,0.011248328,0.0083007915,0.02633545,-0.012642792,0.023169786,-0.05458184,0.03748315,0.016296422,-0.02461411,0.045325395,0.018728953,0.10087687,0.0741355,0.013631429,-0.06463976,0.08628754,-0.01912228,-0.0903804,0.057937752,-0.102498494,-0.038617194,0.04727699,0.043066647,0.012701897,-0.031021707,0.016924698,-0.030505005,-0.02915023,-0.034584325,0.02381984,-0.07165447,0.058129843,0.08695887,0.033921167,0.059497427,-0.020917984,-0.008030744,0.08475497,-0.05578953,-0.040373325,0.074932225,0.0007899265,0.059040066,-0.09008762,0.034451175,-0.04381397,0.09860638,0.005757997,0.03692712,0.041338786,-0.017298136,-0.046168208,-0.051290113,-0.013771481,-0.01696602,0.023087787,0.01718015,0.0013392102,0.052912414,0.01696761,0.063280016,-0.1526469,-0.007016121,-0.093494125,-0.027410831,-0.05503731,-0.048402786,0.024701718,0.028929867,-0.055019084,-0.015250815,-0.013195943,-0.021976016,-0.056933787,-0.020405777,-0.015824726,0.01424083,-0.032811888,0.030652868,0.01492064,0.10916117,0.12332647,-0.013612516,0.024659742,0.07119228,-0.010600003,-0.05893728,0.010343551,0.021192083,-0.010872305,-0.04988027,0.013676287,-1.1563897e-8,-0.062062934,0.0048949015,-0.04481351,0.021870038,0.093440734,0.07049208,-0.033349432,-0.029045964,-0.04572438,0.12527157,0.03183197,0.05687527,0.028921654,-0.013737699,0.024316529,0.0028219547,-0.0019689556,-0.008950844,0.05979234,0.0718772,0.014013006,-0.033784963,0.0028705378,-0.011486769,-0.012574985,-0.040353533,-0.045968752,0.013253078,-0.013288048,0.0077953744,0.0077957413,0.112835534,-0.034299303,-0.01993663,-0.0357279,0.010019326,0.017874451,-0.013488422,-0.0044261427,0.059884507,0.005618065,0.12549663,0.029228112,-0.03833123,-0.024151055,0.0034006755,0.058315456,-0.09857935,0.09229824,-0.06263476,-0.04315847,-0.0015143629,0.057568174,0.033481687,0.016794628,0.07099001,0.014082042,-0.08191792,-0.042998258,0.040871494,0.1388252,-0.0641121,0.024969917,-0.06848822]
lion = [-0.052347623,0.06600294,-0.068091184,0.09499395,-0.027918171,-0.0582941,0.051395744,-0.022421783,0.025851093,0.017970672,-0.037980065,-0.11119092,-0.04492464,-0.0037051875,0.0052331225,-0.03337184,-0.010758403,-0.06399149,-0.0486153,-0.060932197,-0.0586343,0.025884436,-0.0031494533,0.02271689,-0.08961782,0.016098892,-0.08266315,0.011704116,0.0051430603,-0.13229273,-0.041074682,-0.03065579,0.007954663,0.0063774604,-0.087713204,-0.09448998,0.028425721,-0.04825744,0.0038931146,0.0010242971,-0.035032887,-0.0122656105,0.028874498,-0.041676708,-0.069603704,-0.033713236,-0.04829606,0.0059769545,-0.015099709,0.11940327,-0.030127663,-0.005377438,-0.09128438,-0.04558311,0.025648057,0.035062812,-0.01760292,-0.058740314,0.006134028,0.04948019,0.050109643,0.050280243,-0.028602786,0.10359989,-0.030443734,-0.05031092,-0.018092863,-0.009892917,-0.037178013,-0.05641927,-0.00619455,-0.08149883,0.052683868,-0.03604376,-0.0016369649,-0.0064220848,0.16312806,-0.052375555,0.084718384,-0.016106147,0.0025569273,0.008995177,-0.08281328,0.026339816,0.064159974,-0.019265857,-0.011170411,0.02314691,-0.05235367,-0.0030673456,0.034814626,-0.06796918,0.054272782,0.08210706,-0.11830302,0.08720782,0.07765363,-0.09111599,-0.09004476,0.23222649,-0.06074409,0.017528942,0.061397616,0.024322681,0.08867825,-0.031472273,-0.023794029,0.04675054,-0.008309109,0.02610948,0.033066053,-0.0072839996,-0.09366835,0.079978384,0.07644061,-0.0054024784,-0.07871485,-0.079051524,-0.0010394249,0.031966683,0.012010225,0.020079104,-0.0434401,-0.04265281,0.02621226,-0.008959511,0.01160524,-4.199551e-33,0.014741696,-0.08182745,0.07092019,-0.104930416,0.009277172,-0.017105965,0.025796913,0.09403956,-0.049305514,0.08002,-0.036589198,0.03489712,-0.06289699,0.049104776,0.05857148,0.0064041317,-0.010149852,0.00855265,-0.05009303,0.067665294,0.037261102,0.112621926,-0.022140972,-0.03234392,0.031360373,-0.021227852,-0.08066045,-0.07877548,-0.010576719,0.0555842,0.020945292,-0.03810132,-0.037491772,-0.010063753,-0.0040620277,-0.073844716,-0.00325441,-0.100285284,-0.015314189,0.016111542,0.017550237,0.05349244,-0.061702207,0.007073124,0.0267348,0.034979574,0.032880086,-0.014146272,-0.07308931,0.055046856,-0.040623117,0.037589345,0.035455193,0.031842716,-0.03525713,0.038249537,0.065610036,-0.004759952,0.019120352,-0.029107535,0.032665256,0.014049728,0.057056442,0.015823202,0.11204194,-0.046475895,0.05638322,-0.038852554,-0.0020817558,-0.044738833,-0.018573305,0.038473513,0.086497135,-0.053482533,0.055750113,-0.05900748,0.026291722,0.08221408,-0.06971077,-0.03832821,0.029718062,0.07349519,0.01861295,0.019343762,0.04832655,0.0652818,-0.017707063,-0.047592584,-0.03433775,-0.048576493,-0.032239426,0.05021882,0.058349915,-0.07272967,-0.012608294,3.276578e-33,0.009740147,-0.03409539,0.029667484,0.036165014,0.01822561,0.042137925,-0.010273229,0.069398314,-0.08273979,0.037784558,-0.04553135,0.06843985,0.09370985,-0.046199057,0.057065435,-0.034622498,0.048754778,0.018331576,0.03087571,0.0074408026,-0.028125238,-0.032951314,-0.050628077,-0.03428054,0.029041711,-0.034698818,-0.018387944,-0.06404806,-0.05222108,-0.061894517,-0.0077350517,0.044568542,0.026454534,-0.03089354,0.054453705,-0.0007726297,-0.016360246,-0.010995347,-0.048590884,-0.011886369,0.046413995,-0.006131815,0.015803758,0.15025915,0.049311157,0.06531782,-0.03816419,0.061369315,0.032392967,0.058435388,-0.051736493,-0.058704074,0.0064189183,-0.06290436,0.03426619,0.019384505,0.009755742,-0.07505814,0.028477434,0.04525746,-0.013744479,0.034789268,-0.051803138,0.022508701,-0.027568456,0.027941585,-0.042519648,0.032118116,0.010223115,0.0035206524,0.070784315,0.0023557015,-0.04898625,-0.017483117,-0.011468963,0.030044405,0.020041024,-0.03223503,0.010129431,0.015491024,0.03646398,-0.04870026,0.058550216,0.059797388,0.0016104521,-0.05227963,0.06314692,0.03784554,-0.009211694,0.037267763,0.011054084,-0.019844271,0.040336754,-0.074851826,0.0036623438,-1.1783615e-8,-0.027901867,0.006098677,-0.04385833,0.026426908,0.038625125,0.0758251,-0.060797416,-0.06372574,0.027946286,0.06254754,0.039226145,0.010787519,-0.03561551,0.07564017,-0.05904193,0.046687823,0.0061013913,-0.030937074,0.020840283,0.077779554,-0.056667563,0.0146405725,0.01605085,-0.056216218,0.017944595,-0.020689761,-0.05104634,0.004759551,0.06369166,0.012600901,-0.07302585,0.038078796,-0.049389385,0.032434832,0.016782276,-0.00796181,0.034380924,-0.02658265,0.03209965,-0.060337603,0.08996235,0.042017914,0.025643095,-0.05722192,-0.011309183,0.050862283,0.0063682985,-0.08606512,-0.028630858,-0.092791155,-0.026244609,0.018897947,0.023135124,0.016626023,0.0032595817,0.062220387,-0.0011331002,0.0027809022,-0.033333495,0.039280966,0.1738276,0.026122315,0.012003367,0.07720261]
kitten = [-0.022371808,0.023073789,-0.024457,0.029665366,-0.055454634,-0.021883616,0.09633037,0.041377064,0.035718635,0.010809258,-0.024935069,-0.08573223,-0.070663586,0.0392535,-0.05643997,-0.030452197,-0.022215618,-0.0605054,-0.031262882,-0.03801051,-0.061749168,0.04655634,-0.0316772,0.01627655,-0.0549001,0.062622644,-0.0864425,-0.007874477,-0.0050531398,-0.035066217,-0.05778685,-0.01756082,0.07881172,0.04189086,-0.092609696,-0.028873473,-0.030983448,0.00048402714,0.08162459,0.03856072,0.00090686936,-0.027660424,-0.029156553,0.014345244,0.03825698,0.0317028,0.07409206,-0.051706795,0.07370757,0.0335378,-0.08140658,-0.008600537,-0.07207154,0.04534365,0.001096669,-0.01652229,0.05205094,0.007960105,-0.0038962613,-0.020925118,-0.01963315,0.005781137,0.030373946,0.04131186,0.043516427,0.04612634,-0.06175959,-0.02469966,0.053974267,0.005144348,0.070149325,0.06549221,-0.014875086,0.029207116,-0.038444214,-0.013887857,0.12288133,0.05035741,0.11261591,0.03439388,-0.005894454,0.0045530535,-0.06490736,0.02833695,0.010357571,0.046150915,-0.06458247,0.012546747,-0.08617302,0.04309304,0.031745736,0.054250292,0.02966407,0.033998005,-0.1479516,0.0064685117,0.08232668,-0.074045196,-0.09113611,0.21706468,0.02049961,0.03518524,-0.04767136,0.063307844,0.0058970465,-0.017809222,0.016201133,0.031833034,-0.010852325,0.0014517555,-0.047526926,-0.036110908,0.0057118074,0.062702455,0.033548422,-0.09197228,-0.029930005,0.008033804,0.08775477,0.05222521,0.061790682,0.0047272546,0.03902144,-0.011960418,-0.06714013,-0.10862289,-0.043208525,-3.4510082e-33,-0.005685265,-0.091569684,0.037044436,0.0337668,0.07275369,0.036734793,0.027391693,0.03756987,-0.0807105,0.020198924,-0.023914471,-0.0279498,-0.06593742,-0.044970427,0.042089317,-0.007881395,-0.02663132,-0.035566002,0.02740124,-0.00077905343,0.011444414,0.04731973,0.053132344,0.082479,-0.01117319,-0.078820296,-0.018427866,-0.04035342,-0.033953782,-0.011582275,0.04639716,-0.015270279,0.05404343,-0.01606842,-0.09696546,-0.13287652,-0.0040688636,-0.093538426,-0.006757072,0.02723152,0.038489062,0.010648111,0.044273444,0.02689569,0.011994557,0.013099151,0.04819351,0.12314913,-0.009932333,-0.020764342,0.05367488,-0.021305272,-0.015419547,-0.053425755,-0.006580858,0.002771914,-0.021528717,-0.05641686,-0.06417188,0.09217226,0.07670099,0.027308816,0.07291559,-0.0006835452,0.0012003903,-0.061966985,0.003432962,-0.027159818,0.090970226,-0.007637545,-0.018213362,0.016984189,0.04872711,-0.08193441,-0.00013774211,-0.011430981,0.01935955,-0.03777408,-0.06458825,-0.035226565,0.008425948,-0.021057563,0.07980342,0.068482436,-0.005436867,0.040935304,-0.044230167,-0.08320597,0.0040697292,0.06931593,-0.056618035,0.0277933,0.002348691,-0.08518585,0.07234516,3.551734e-33,0.013725487,-0.046168145,-0.033866525,0.023924744,-0.056624237,0.037105173,0.025313037,0.015726738,-0.013004082,0.12969469,-0.03401536,0.0031154167,0.097106054,-0.049126387,0.025253888,0.08204685,0.045069687,-0.038968213,0.013884618,-0.01429633,-0.058289822,-0.016613267,-0.053882975,0.0067733587,0.0052493224,0.002237552,0.0010822403,0.028326176,0.043116104,-0.10757652,0.00936595,-0.017618932,0.0051658326,0.004216178,0.04015349,0.11371099,-0.0023081827,-0.051773578,-0.014837854,-0.009465329,0.06310992,0.013435731,-0.052783,0.073539056,0.0065905764,0.013607279,-0.052688822,0.06901829,0.084530115,0.020183379,-0.048231382,-0.06968074,-0.050570775,0.003689383,0.0034989612,-0.03980707,-0.0033606654,0.0021650675,0.06653971,-0.010389157,0.06421706,0.04152017,-0.076406725,0.042826533,-0.052617088,-0.041606747,-0.026678352,-0.014611302,-0.031340074,-0.017637417,0.15533605,0.019442419,-0.039100528,-0.02879286,-0.07162956,0.0723857,0.038291298,0.0171035,-0.036511544,0.008132774,-0.019154038,0.038354494,0.020546928,0.036090706,-0.09063486,-0.078665204,0.13996395,0.07309401,-0.035744336,0.013735348,0.020882273,0.007415606,-0.008830264,-0.08425293,0.009202526,-1.1436219e-8,-0.03270978,0.0029511808,-0.08472894,-0.008350981,0.029303323,0.05845227,-0.0031393096,-0.02339549,0.017730352,-0.0053910553,0.01411887,-0.06297909,0.027935298,0.0677412,0.048283324,0.03731386,-0.011872466,0.009525792,0.02097987,0.033803977,-0.075527355,0.04639147,-0.08333615,0.013909151,-0.041952025,-0.090945035,-0.03747992,0.077096656,0.016982565,-0.0051650214,-0.067697,-0.011033064,0.004199205,-0.09944321,-0.014033254,0.024684435,0.029284952,-0.07435119,0.06896775,-0.05495394,0.00039502655,0.0029922118,0.06697257,-0.06572328,-0.044204105,-0.040802833,0.048564903,-0.04380039,0.001210537,-0.024194485,0.08436737,0.032119162,0.05106511,0.0635153,0.017086642,0.017540717,-0.048993643,0.027007764,-0.012272347,0.06604709,0.12151364,0.045274828,0.054008745,0.0119850645]
dog = [-0.053127173,0.014129783,0.0071834642,0.06877906,-0.07815561,0.010297088,0.102251515,-0.01216958,0.09513144,-0.029969713,0.0023248212,-0.0648245,-0.0028254788,0.0064172484,-0.00403375,-0.030463668,-0.04769255,-0.019087201,-0.059531447,-0.10413801,-0.08610042,0.036099184,-0.025392175,0.0013366184,-0.07133566,0.06171227,0.017037764,-0.056747995,0.024786996,-0.077937104,-0.03257987,-0.008782279,-0.011816178,0.038041126,-0.056910053,-0.053386178,0.004945784,0.032522272,0.07277516,0.033185154,0.02464143,-0.083290465,-0.015453737,-0.048114866,-0.0034445582,0.004287242,-0.036066297,-0.051936917,0.015415637,0.0033627732,-0.010201713,0.047151912,-0.04015471,-0.009262611,-0.03474902,-0.036913343,-0.040666737,0.017523391,-0.009466804,-0.053709425,0.010926722,0.016251335,0.013869728,0.028160285,0.040214844,0.020952137,-0.014698406,-0.0016230288,-0.0051680165,0.012057663,0.045453645,0.013103767,0.070467785,-0.030912232,0.030270852,-0.1087719,0.05550388,-0.01743967,0.16437209,0.051458348,-0.027854921,-0.03000179,-0.056845594,0.056903806,0.051078383,0.015297698,-0.0012257678,0.02385994,-0.06342136,0.028568292,-0.05538952,-0.035246465,0.03034843,0.026682869,-0.08338664,0.018573763,-0.035012193,-0.08295873,-0.07179471,0.19795758,0.01633866,0.044760425,-0.0036737807,-0.03839507,0.05341411,-0.0036137737,-0.04314179,0.06347609,-0.013079783,-0.019579919,-0.045234263,0.020740913,-0.05657746,0.05726308,0.0557237,0.021306332,-0.10086276,-0.03429051,0.029231679,-0.03331771,0.028860996,0.030214394,-0.052112512,0.008364239,-0.01685459,-0.08435341,0.01118796,-5.938997e-33,0.030560808,-0.085231386,0.0024765371,-0.041397844,-0.042259153,0.04102274,0.029409774,0.036412306,-0.12122637,0.013533209,-0.014234837,0.031046793,-0.021575106,0.016238851,0.11229251,-0.0067959684,-0.0017608003,0.053101137,0.032751825,-0.03769815,-0.046912875,0.061964452,0.06362556,0.04989983,-0.0075604487,-0.021412618,-0.037594642,-0.0829842,-0.026426945,0.036138985,0.041330107,0.014601796,0.07350069,0.00066684355,-0.081367,-0.05567413,-0.042212762,-0.09679145,-0.040282622,0.028749038,0.1291665,0.010313694,0.024834003,0.017367769,-0.02724448,-0.005038514,0.015573671,0.03436311,-0.044253647,0.020888291,0.027635902,-0.014084881,0.028773114,-0.021319708,0.00866621,0.009999512,0.002819221,-0.02363404,0.012880111,0.066664755,0.06907869,0.08237574,0.009008921,-0.014065214,0.09122715,-0.12189071,-0.045508705,-0.0181745,-0.022219473,0.021698836,-0.03878902,-0.019074831,0.079553224,-0.015838439,0.06864844,-0.0154359285,0.022777595,0.025133515,-0.03127067,-0.033634953,-0.021362226,-0.010045977,0.0055371555,0.049142398,-0.021579206,0.063703224,-0.019676942,-0.030058369,0.005844785,0.045282472,-0.04589753,-0.04936118,0.08693275,0.027196608,0.090798855,3.4475122e-33,0.062532015,0.029071169,0.00029525015,0.09160385,-0.030267654,0.0049796794,-0.02547511,0.06672206,-0.03421631,0.04798319,-0.033982627,0.007916957,0.10796033,0.008964775,0.007382584,0.08846541,0.003639775,-0.030546475,0.021758141,-0.0046311426,-0.14476119,0.01161343,0.01831796,-0.02595096,-0.05191631,0.03949207,0.037336174,-0.014980785,-0.022576606,-0.04888132,-0.0067262473,-0.039659023,-0.041009776,-0.028365923,0.010649289,0.15872094,0.047608726,-0.047298037,-0.06292891,0.008348204,0.059938725,0.019115767,-0.03239848,0.111239344,0.016363088,0.052667323,-0.017614879,-0.00598157,0.053081445,0.018707877,-0.04750299,-0.014151515,0.030387338,-0.07306211,-0.012404361,0.004599777,-0.09512797,0.018934503,-0.029047411,-0.0051085833,-0.0028861098,0.06991964,0.012384721,0.121917225,-0.10499913,-0.053846423,-0.012673515,-0.028261526,0.049862247,-0.07674974,0.024259672,0.04529221,-0.028840259,0.010150866,-0.010216872,0.03128274,-0.046499796,0.0042539206,0.0076975264,-0.0064783823,-0.078131355,-0.06523765,-0.04744238,0.010397574,-0.05631948,-0.0110725425,0.0021607627,0.06392043,-0.013325774,-0.0300606,-0.009806091,0.0551403,-0.021538062,-0.053546358,-0.028550332,-1.332399e-8,-0.028899115,-0.02904847,-0.042777095,-0.019308446,0.09982276,0.06952208,-0.03013539,-0.04035026,-0.0068445634,0.026076859,0.044047233,-0.016792303,-0.07014283,0.013504975,0.046356514,-0.015053794,-0.05332495,0.03994635,0.06294708,0.07736516,-0.050828353,0.030344814,0.055484165,0.002142581,-0.05141306,-0.03602167,0.04553177,0.105663456,-0.08208312,0.038041435,-0.022720974,0.14089237,-0.07600159,-0.030181589,-0.0040423186,-0.06973481,0.07623586,-0.07901917,0.024577124,0.0341695,0.05038124,0.15225497,-0.020201651,-0.0787306,-0.00044399107,0.062299687,0.02674826,-0.12157516,-0.028068407,-0.056232903,-0.09833085,-0.0076753506,0.028459698,0.068956025,0.014856709,0.0050617224,-0.013172522,-0.047952686,-0.016495524,0.0366687,0.11141257,0.029869484,0.024000183,0.10995536]

cosine = np.dot(kitten, cat)/(norm(kitten)*norm(cat))
print("Cat/Kitten Cosine Similarity:", cosine)

cosine = np.dot(kitten, wolf)/(norm(kitten)*norm(wolf))
print("Wolf/Kitten Cosine Similarity:", cosine)

cosine = np.dot(kitten, dog)/(norm(kitten)*norm(dog))
print("Dog/KittenCosine Similarity:", cosine)