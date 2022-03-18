#hint: annotates chart with elliot wave numbers.
##################################################

script oneUpOneDnLook {
input origin=0.0;
input levelOne=0.0;
input wave2Factor=0.0;

def bigNum=power(10,7);
def bigNumSqd=bigNum*BigNum;

def w2threshold=levelOne-(levelOne-origin)*wave2Factor;

  

plot return= 
    if high>=high[1] then 0
    else if high[1]!=levelOne then 0
    else (fold i=0 to 999 with ii=low while !floor(ii/bigNumSqd) do 
        if isnan(getvalue(close,-i)) then bigNumSqd
        else if getvalue(low,-i) <= origin then bigNumSqd+1
        else if ii>w2threshold and getvalue(high,-i)>=levelOne then bigNumSqd
        else if ii<=w2threshold and getvalue(high,-i)>=ii+levelOne-origin then bigNumSqd
        else if getvalue(low,-i)<ii then getvalue(low,-i)      
        else ii) %bigNumSqd
;

}
##################################################
script oneUpOneDnLookDbg {
input origin=0.0;
input levelOne=0.0;
input wave2Factor=0.0;

def bigNum=power(10,7);
def bigNumSqd=bigNum*BigNum;

def w2threshold=levelOne-(levelOne-origin)*wave2Factor;
  

plot return= 
    if high>=high[1] then 1
    else if high[1]!=levelOne then 2
    else (fold i=0 to 999 with ii=low while !floor(ii/bigNumSqd) do 
        if isnan(getvalue(close,-i)) then bigNumSqd+3
        else if getvalue(low,-i) <= origin then bigNumSqd+4
        else if ii>w2threshold and getvalue(high,-i)>=levelOne then bigNumSqd+5
        else if ii<=w2threshold and getvalue(high,-i)>=ii+levelOne-origin then bigNumSqd+6
        else if getvalue(low,-i)<ii then getvalue(low,-i)      
        else ii) %bigNumSqd
;

}

##################################################
script oneDnOneUpLook {
input origin=0.0;
input levelOne=0.0;
input wave2Factor=0.0;

def bigNum=power(10,7);
def bigNumSqd=bigNum*BigNum;
def w2threshold=levelone+(origin-levelOne)*wave2Factor;

plot return= 
    if low<=low[1] then 0
    else if low[1]!=levelOne then 0
    else (fold i=0 to 999 with ii=high while !floor(ii/bigNumSqd) do 
        if isnan(getvalue(close,-i)) then bigNumSqd
        else if getvalue(high,-i) >= origin then bigNumSqd+1
        else if ii<w2threshold and getvalue(low,-i)<=levelOne then bigNumSqd
        else if ii>=w2threshold and getvalue(low,-i)<=ii-origin+levelOne then bigNumSqd
        else if getvalue(high,-i)>ii then getvalue(high,-i)      
        else ii) %bigNumSqd
;

}##################################################
script oneDnOneUpLookDbg {
input origin=0.0;
input levelOne=0.0;
input wave2Factor=0.0;

def bigNum=power(10,7);
def bigNumSqd=bigNum*BigNum;

plot return= 
    if low<=low[1] then 1
    else if low[1]!=levelOne then 2
    else (fold i=0 to 999 with ii=high while !floor(ii/bigNumSqd) do 
        if isnan(getvalue(close,-i)) then bigNumSqd+3
        else if getvalue(high,-i) >= origin then bigNumSqd+4
        else if ii<levelOne*(1+Wave2Factor) and getvalue(low,-i)<=levelOne then bigNumSqd+5
        else if ii>=levelOne*(1+Wave2Factor) and getvalue(low,-i)<=ii-origin+levelOne then bigNumSqd+6
        else if getvalue(high,-i)>ii then getvalue(high,-i)      
        else ii) %bigNumSqd
;

}

##################################################
script oneUpLook {
    input iOrg = 0.0;
    input iL1 = 0.0;
    input wave2factor = 0.5;
    def bigNum = Power(10, 7);
    def bigNumSqd = bigNum * bigNum;

    def twoDn = 
        (fold y = 1 to 1000 with yy=low while !Floor(yy / bigNumSqd) do
            if yy < iOrg  then bigNumSqd 
            else if IsNaN(GetValue(close, -y)) then bigNumSqd
            else if GetValue(high, -y) > iL1 and AbsValue(GetValue(high, -y) - (yy % bigNum)) >= AbsValue(iL1 - iOrg) then bigNumSqd + yy
            else if GetValue(low, -y) <= (yy % bigNum) then y * bigNum + GetValue(low, -y)
            else yy
        )
    ;
    def twoDnOff = Floor((twoDn % bigNumSqd) / bigNum);
    def twoDnLvl = GetValue(low, -twoDnOff);

    def maybeOneUpOff = #looks for first high pivot above iL1
        (fold x = 1 to 1000 with xx while !Floor(xx / bigNum) do
            if IsNaN(GetValue(close, -x)) then bigNum
            else if GetValue(low, -x) < iOrg then bigNum
            else if x == twoDnOff then bigNum + x
            else if IsNaN(GetValue(high, -x - 1)) then bigNum
            else if GetValue(high, -x) > iL1 and GetValue(high, -x) > GetValue(high, -x - 1) then bigNum + x
            else 0
        ) % bigNum;


    plot sigup = 
        if high >= high[1] then 1 
        else if AbsValue(twoDnLvl - iL1) / AbsValue(iL1 - iOrg) < wave2factor then 2
        else if maybeOneUpOff and maybeOneUpOff < twoDnOff then 3
        else 0
    ;
    plot off2 = twoDnOff;
    plot dn2 = twoDnLvl;
    plot upOff = maybeOneUpOff;


}#end oneUpLook

#####################################
script oneDnLook {
    input iOrg = 0.0;
    input iL1 = 0.0;
    input wave2factor = 0.5;
    def bigNum = Power(10, 7);
    def bigNumSqd = bigNum * bigNum;

    def twoUp = 
        (fold y = 1 to 1000 with yy=high while !Floor(yy / bigNumSqd) do
            if yy > iOrg then bigNumSqd 
            else if IsNaN(GetValue(close, -y)) then bigNumSqd
            else if GetValue(low, -y) < iL1 and AbsValue(GetValue(low, -y) - (yy % bigNum)) >= AbsValue(iL1 - iOrg) then bigNumSqd + yy
            else if GetValue(high, -y) >= (yy % bigNum) then y * bigNum + GetValue(high, -y)
            else yy
        )
    ;
    def twoUpOff = Floor((twoUp % bigNumSqd) / bigNum);
    def twoUpLvl = GetValue(low, -twoUpOff);

    def maybeOneDnOff = #looks for first low pivot below iL1
        (fold x = 1 to 1000 with xx while !Floor(xx / bigNum) do
            if IsNaN(GetValue(close, -x)) then bigNum
            else if GetValue(high, -x) > iOrg then bigNum
            else if x == twoUpOff then bigNum + x
            else if IsNaN(GetValue(low, -x - 1)) then bigNum
            else if GetValue(low, -x) < iL1 and GetValue(low, -x) < GetValue(low, -x - 1) then bigNum + x
            else 0
        ) % bigNum;


    plot sigup = 
        if low <= low[1] then 1 
        else if AbsValue(twoUpLvl - iL1) / AbsValue(iL1 - iOrg) < wave2factor then 2
        else if maybeOneDnOff and maybeOneDnOff < twoUpOff then 3
        else 0
    ;
    plot off2 = twoUpOff;
    plot dn2 = twoUpLvl;
    plot upOff = maybeOneDnOff;

} #end oneDnLook


################################
script threeUpLook {
    input levelOne = 0.0;
    input levelTwo = 0.0;
    input levelThree = 0.0;
    input wave4Factor = 0.2;
    input wave5Limit = 0.0;

    def bigNum = Power(10, 7);
    def bigNumSqd = bigNum * bigNum;

    def fourDn = 
        (fold z = 1 to 1000 with zz=low while !Floor(zz / bigNumSqd) do
            if IsNaN(GetValue(close, -z)) then bigNumSqd + zz
            else if GetValue(high, -z) > levelThree and GetValue(low, -z) < (zz % bigNum) then bigNumSqd * 11 #spanner
            else if GetValue(high, -z) > levelThree then bigNumSqd + zz 
            else if GetValue(low, -z) <= (zz % bigNum) then z * bigNum + GetValue(low, -z)
            else zz
        ) 
    ;
    def fourDnOff = Floor((fourDn % bigNumSqd) / bigNum);
    def fourDnLvl = GetValue(low, -fourDnOff) ;

    def fiveUp = 
        (fold y = 1 to 1000 with yy=high while !Floor(yy / bigNumSqd) do
            if IsNaN(GetValue(close, -y)) then bigNumSqd + yy
            else if GetValue(high, -y) >= (yy % bigNum) then y * bigNum + GetValue(high, -y)
            else if GetValue(low, -y) < fourDnLvl then bigNumSqd + yy
            else yy
        )
   ;
    def fiveUpOff = Floor((fiveUp % bigNumSqd) / bigNum);
    def fiveUpLvl = GetValue(high, -fiveUpOff);

    plot return = if high >= high[1] then 10
        else if high[1] != levelThree then 2
        else if fourDn / bigNumSqd == 11 then 3   #spanning bar 
        else if fourDnLvl and fourDnLvl < levelTwo then 0
        else if fourDnLvl and fourDnLvl<levelOne then 1
        else if fourDnLvl and  
            AbsValue(fourDnLvl - levelThree) / AbsValue(levelThree - levelTwo) < wave4Factor then 4
        else if fourDnLvl and fiveUpLvl and AbsValue(fiveUpLvl - fourDnLvl) > wave5Limit then 5
        else 0;

    plot level_4 =  fourDnLvl;
    plot offset_4 =  fourDnOff ;
    plot level_5 = fiveUpLvl;
    plot offset_5 = fiveUpOff;
} #end threeUpLook

#######################################
script threeDnLook {
    input levelOne = 0.0;
    input levelTwo = 0.0;
    input levelThree = 0.0;
    input wave4Factor = 0.2;
    input wave5Limit = 0.0;


    def bigNum = Power(10, 7);
    def bigNumSqd = bigNum * bigNum;

    def fourUp = 
        (fold y = 1 to 1000 with yy=high while !Floor(yy / bigNumSqd) do
            if IsNaN(GetValue(close, -y)) then bigNumSqd + yy
            else if GetValue(low, -y) < levelThree and GetValue(high, -y) > yy % bigNum then bigNumSqd * 11 
            else if GetValue(low, -y) < levelThree then bigNumSqd + yy 
            else if GetValue(high, -y) >= (yy % bigNum) then y * bigNum + GetValue(high, -y)
            else yy
        )
    ;
    def fourUpOff = Floor((fourUp % bigNumSqd) / bigNum);
    def fourUpLvl = GetValue(high, -fourUpOff);

    def fiveDn = 
        (fold x = 1 to 1000 with xx=low while !Floor(xx / bigNumSqd ) do
            if IsNaN(GetValue(close, -x)) then bigNumSqd + xx 
            else if GetValue(low, -x) <= (xx % bigNum) then x * bigNum + GetValue(low, -x)
            else if GetValue(high, -x) > fourUpLvl then bigNumSqd + xx 
            else xx
        )
    ;
    def fiveDnOff = Floor((fiveDn % bigNumSqd) / bigNum);
    def fiveDnLvl = GetValue(low, -fiveDnOff);

    plot return = if low <= low[1] then 10 
        else if low[1] != levelThree then 2
        else if fourUp / bigNumSqd == 11 then 3
        else if fourUpLvl and fourUpLvl > levelTwo then 0 #this shouldn't happen but.. let case fourUp get it.
        else if fourUpLvl and fourUpLvl>=levelOne then 1 # don't go to fourUp
        else if fourUpLvl and 
            AbsValue(fourUpLvl - levelThree) / AbsValue(levelThree - levelTwo) < wave4Factor then 4
        else if fourUpLvl and fiveDnLvl and AbsValue(fiveDnLvl - fourUpLvl) > wave5Limit then 5
        else 0;

    plot level_4 =  fourUpLvl;
    plot offset_4 = fourUpOff;
    plot level_5 = fiveDnLvl;
    plot offset_5 = fiveDnOff;
} #end threeDnLook
############################################
script upLook {
    input lowLevel = 0.0;

    plot return = 
if high >= high[1] and low >= lowLevel then 1
else if low < lowLevel then 0
else (fold a = 1 to 1000 with aa while !aa do 
        if IsNaN(GetValue(low, -a)) then 1
        else if GetValue(high, -a) >= high[1] and GetValue(low, -a) >= lowLevel then 1
        else if GetValue(low, -a) < lowLevel then 10
        else 0) != 10;

}

#######################
script downLook {
    input highLevel = 0.0;

    plot return =
if low <= low[1] and high <= highLevel then 1
else if high > highLevel then 0
else (fold a = 1 to 1000 with aa while !aa do 
        if IsNaN(GetValue(low, -a)) then 1
        else if GetValue(low, -a) <= low[1] and GetValue(high, -a) <= highLevel then 1
        else if GetValue(high, -a) > highLevel then 10
        else 0) != 10;
}
#######################
script fiveUpLook {
    input levelThree = 0.0;
    input levelFour = 0.0;
    input levelFive = 0.0;

    def bigNum = Power(10, 7);
    def bigNumSqd = bigNum * bigNum;


    def fiveUp = 
    fold b = 0 to 999 with bb while !Floor(bb / bigNum) do
        if IsNaN(GetValue(close, -b)) then bigNum + bb + b
        else if GetValue(low, -b) <= levelFour then bigNum + bb + 1000 + b
        else if GetValue(high, -b) >= levelFive then bigNum + bb + 10000 + b
        else if GetValue(low, -b) <= levelThree then (bb % 100000) + 100000
        else bb;
    ;
    def fiveUpIdx = fiveUp % 1000;
    def fourBreak = fiveUp % 10000 >= 1000;
    def fiveBreak = fiveUp % 100000 >= 10000;
    def threeBreak = fiveUp % bigNum >= 100000;


    plot return =
    if high >= high[1] then 1
    else if fourBreak then 0
    else if fiveBreak then 5
    else if threeBreak then 0
    else if fiveUpIdx > 10 then 0
    else 1;



    plot scan5up = fiveUp;
}
#######################
script fiveDnLook {
    input levelThree = 0.0;
    input levelFour = 0.0;
    input levelFive = 0.0;

    def bigNum = Power(10, 7);
    def bigNumSqd = bigNum * bigNum;


    def fiveDn =
    fold b = 0 to 999 with bb while !Floor(bb / bigNum) do
        if IsNaN(GetValue(close, -b)) then bigNum + bb + b
        else if GetValue(high, -b) >= levelFour then bigNum + bb + 1000 + b
        else if GetValue(low, -b) <= levelFive then bigNum + bb + 10000 + b
        else if GetValue(high, -b) >= levelThree then (bb % 100000) + 100000
        else bb;
    ;
    def fiveDnIdx = fiveDn % 1000;
    def fourBreak = fiveDn % 10000 >= 1000;
    def fiveBreak = fiveDn % 100000 >= 10000;
    def threeBreak = fiveDn % bigNum >= 100000;


    plot return =
    if low<=low[1] then 1
    else if fourBreak then 0
    else if fiveBreak then 5
    else if threeBreak then 0
    else if fiveDnIdx > 10 then 0
    else 1;



    plot scan5dn = fiveDn;
}
#######################
script threeUpOneDnLook {
    input levelOne = 0.0;
    input levelTwo = 0.0;
    input levelThree = 0.0;

    def bigNum = Power(10, 7);
    def bigNumSqd = bigNum * bigNum;

    def fourDn = 
        (fold z = 1 to 1000 with zz=low while !Floor(zz / bigNumSqd) do
            if IsNaN(GetValue(close, -z)) then bigNumSqd*12 + zz
            else if GetValue(high, -z) > levelThree and GetValue(low, -z) < (zz % bigNum) then bigNumSqd * 11 #spanner
            else if GetValue(high, -z) > levelThree then bigNumSqd * 10 + zz 
            else if GetValue(low, -z) <= (zz % bigNum) then z * bigNum + GetValue(low, -z)
            else zz
        ) 
    ;
    def fourDnOff = Floor((fourDn % bigNumSqd) / bigNum);
    def fourDnLvl = GetValue(low, -fourDnOff) ;

    plot return = if high >= high[1] then 0
        else if high[1] != levelThree then 0
        else if fourDn / bigNumSqd == 11 then 0   #spanning bar 
        else if fourDnLvl and fourDnLvl < levelTwo then 2
        else if fourDnLvl and fourDnLvl<levelOne and floor(fourDn/bigNumSqd)==12 then 1
        else if Floor(fourDn / bigNumSqd) == 10 then 0 #>=L2 and recrossed L3 
        else if fourDnLvl and fourDnLvl < levelOne then 0 #btw L2 and L1 maybe a oneDn
        else 0;

    plot level_4 =  fourDnLvl ;
    plot offset_4 =  fourDnOff ;

}
#######################
script threeDnOneUpLook {

    input levelOne = 0.0;
    input levelTwo = 0.0;
    input levelThree = 0.0;



    def bigNum = Power(10, 7);
    def bigNumSqd = bigNum * bigNum;

    def fourUp = 
        (fold y = 1 to 1000 with yy=high while !Floor(yy / bigNumSqd) do
            if IsNaN(GetValue(close, -y)) then bigNumSqd*12 + yy
            else if GetValue(low, -y) < levelThree and GetValue(high, -y) > yy % bigNum then bigNumSqd * 11 
            else if GetValue(low, -y) < levelThree then bigNumSqd * 10 + yy 
            else if GetValue(high, -y) >= (yy % bigNum) then y * bigNum + GetValue(high, -y)
            else yy
        )
    ;
    def fourUpOff = Floor((fourUp % bigNumSqd) / bigNum);
    def fourUpLvl = GetValue(high, -fourUpOff);

    plot return = if low <= low[1] then 0
        else if low[1] != levelThree then 0
        else if fourUp / bigNumSqd == 11 then 0   #spanning bar 
        else if fourUpLvl and fourUpLvl > levelTwo then 2
        else if fourUpLvl and fourUpLvl>levelOne and floor(fourUp/bigNumSqd)==12 then 1
        else if Floor(fourUp / bigNumSqd) == 10 then 0 #<=L2 and recrossed L3 
        else if fourUpLvl and fourUpLvl > levelOne then 0 #btw L2 and L1 maybe a oneUp
        else 0;


    plot level_4 =  fourUpLvl;
    plot offset_4 = fourUpOff;


}

##################################################
script twoDnStayOrAdvance {
    input origin = 0.0;
    input levelOne = 0.0;
    input levelTwo = 0.0;

    plot return = if low < levelTwo then 1 else
AbsValue(high - levelTwo) < AbsValue(levelOne - origin) ;
}
##################################################
script twoUpStayOrAdvance {
    input origin = 0.0;
    input levelOne = 0.0;
    input levelTwo = 0.0;

    plot return = if high > levelTwo then 1 else
AbsValue(low - levelTwo) < AbsValue(levelOne - origin) ;
}
#######################################

input startBar = 2;
#hint startBar: indicates the bar number on which to start analysis. rev:1.0.0 5/8/2017
input wave2Factor = 0.25;
#hint wave2Factor: how much of wave1 must be retraced to recognize wave2. 
def wave3Factor = 1.0;
input wave4Factor = 0.25;
#hint wave4Factor: how much of wave3 must be retraced to recognize wave4.
def wave4Overlap = 0.0;
#    input wave5Factor = 1.25;
input summaries = yes;
#hint summaries: controls the display of wave5 summary bubbles.
input diagnostics = no;
#hint diagnostics: displays the inner workings of the finite state analysis. displays wave levels and state transitions.


def bigNum = Power(10, 9);
def formingBar = IsNaN(close[-1]) crosses above 0;
def s1state = {default init, oneUp, oneDn, twoUp, twoDn, threeUp, threeDn, fourDn, fourUp, fiveUp, fiveDn};
def s1org;
def s1L1;
def s1L2;
def s1L3;
def s1L4;
def s1L5;
def s1CC;

switch (s1state[1]){
case init:
    if BarNumber() <= 2 or BarNumber() < startBar
    or (high > high[1] and low < low[1]) 
    or (high > high[1] and low < low[1]) {
        s1state = s1state.init;
        s1org = 0;
        s1L1 = 0;
        s1L2 = 0;
        s1L3 = 0;
        s1L4 = 0;
        s1L5 = 0;
        s1CC = 0;
    } else if high > high[1] {
        s1state = s1state.oneUp;
        s1org = low[1];
        s1L1 = high;
        s1L2 = 0;
        s1L3 = 0;
        s1L4 = 0;
        s1L5 = 0;
        s1CC = 0;
    } else if low < low[1] {
        s1state = s1state.oneDn;
        s1org = high[1];
        s1L1 = low;
        s1L2 = 0;
        s1L3 = 0;
        s1L4 = 0;
        s1L5 = 0;
        s1CC = 0;
    } else {
        s1state = s1state.init;
        s1org = 0;
        s1L1 = 0;
        s1L2 = 0;
        s1L3 = 0;
        s1L4 = 0;
        s1L5 = 0;
        s1CC = 0;
    }
###
case oneUp:
    if oneUpOneDnLook(s1Org[1],s1L1[1],wave2Factor) {
        s1state = s1state.oneDn;
        s1org = Max(s1L1[1], high);
        s1L1 = low;
        s1L2 = 0;
        s1L3 = 0;
        s1L4 = 0;
        s1L5 = 0;
        s1CC = 1;
    } else if oneUpLook( s1org[1], s1L1[1], wave2Factor) {
        s1state = s1state.oneUp;
        s1org = s1org[1];
        s1L1 = Max(high, s1L1[1]);
        s1L2 = 0;
        s1L3 = 0;
        s1L4 = 0;
        s1L5 = 0;
        s1CC = 0;
    } else { #high<high[1]
        s1state = s1state.twoDn;
        s1org = s1org[1];
        s1L1 = s1L1[1];
        s1L2 = low;
        s1L3 = 0;
        s1L4 = 0;
        s1L5 = 0;
        s1CC = 0;
#        s1CC=oneUpOneDnLookDbg(s1Org[1],s1L1[1],wave2Factor);
    }
case oneDn:
    if oneDnOneUpLook(s1Org[1],s1L1[1],wave2Factor) {
        s1state = s1state.oneUp;
        s1org = Min(s1L1[1], low);
        s1L1 = high;
        s1L2 = 0;
        s1L3 = 0;
        s1L4 = 0;
        s1L5 = 0;
        s1CC = 1;
    } else if oneDnLook( s1org[1], s1L1[1], wave2Factor) {
        s1state = s1state.oneDn;
        s1org = s1org[1];
        s1L1 = Min(low, s1L1[1]);
        s1L2 = 0;
        s1L3 = 0;
        s1L4 = 0;
        s1L5 = 0;
        s1CC = 0;
#        s1cc=oneDnOneUpLookdbg(s1Org[1],s1L1[1],wave2Factor);

    } else { #low>low[1] 
        s1state = s1state.twoUp;
        s1org = s1org[1];
        s1L1 = s1L1[1];
        s1L2 = high;
        s1L3 = 0;
        s1L4 = 0;
        s1L5 = 0;
        s1CC = 0;
    }
## 
case twoUp:
    if high > s1org[1] {
        s1state = s1state.oneUp;
        s1org = Min(s1L1[1], low);
        s1L1 = high;
        s1L2 = 0;
        s1L3 = 0;
        s1L4 = 0;
        s1L5 = 0;
        s1CC = 2;
    } else if twoUpStayOrAdvance(s1org[1], s1L1[1], s1L2[1]) {
        s1state = s1state.twoUp;
        s1org = s1org[1];
        s1L1 = s1L1[1];
        s1L2 = Max(s1L2[1], high);
        s1L3 = 0;
        s1L4 = 0;
        s1L5 = 0;
        s1CC = 0;
    } else { #low < s1L1[1]
        s1state = s1state.threeDn;
        s1org = s1org[1];
        s1L1 = s1L1[1];
        s1L2 = s1L2[1];
        s1L3 = low;
        s1L4 = 0;
        s1L5 = 0;
        s1CC = 0;
    }
case twoDn:
    if low < s1org[1] {
        s1state = s1state.oneDn;
        s1org = Max(s1L1[1], high);
        s1L1 = low;
        s1L2 = 0;
        s1L3 = 0;
        s1L4 = 0;
        s1L5 = 0;
        s1CC = 2;
    } else if twoDnStayOrAdvance(s1org[1], s1L1[1], s1L2[1]) {
        s1state = s1state.twoDn;
        s1org = s1org[1];
        s1L1 = s1L1[1];
        s1L2 = Min(s1L2[1], low);
        s1L3 = 0;
        s1L4 = 0;
        s1L5 = 0;
        s1CC = 0;
    } else {
        s1state = s1state.threeUp;
        s1org = s1org[1];
        s1L1 = s1L1[1];
        s1L2 = s1L2[1];
        s1L3 = high;
        s1L4 = 0;
        s1L5 = 0;
        s1CC = 0;
    }
###
case threeUp:
#    if !upLook(s1L2[1]) {
    if threeUpOneDnLook(s1L1[1],  s1L2[1], s1L3[1]) {
        s1state = s1state.oneDn;
        s1org = Max(s1L3[1], high);
        s1L1 = low;
        s1L2 = 0;
        s1L3 = 0;
        s1L4 = 0;
        s1L5 = 0;
        s1CC = 3;

    } else if threeUpLook( s1L1[1],  s1L2[1], s1L3[1], wave4Factor, AbsValue(s1L3[1] - s1L2[1])) {
        s1state = s1state.threeUp;
        s1org = s1org[1];
        s1L1 = s1L1[1];
        s1L2 = s1L2[1];
        s1L3 = Max(s1L3[1], high);
        s1L4 = 0;
        s1L5 = 0;
        s1CC = 0;#threeUpLook( s1L1[1],  s1L2[1], s1L3[1], wave4Factor, AbsValue(s1L3[1] - s1L2[1]));

    } else { #w3>w1 and high<high[1]
        s1state = s1state.fourDn;
        s1org = s1org[1];
        s1L1 = s1L1[1];
        s1L2 = s1L2[1];
        s1L3 = s1L3[1];
        s1L4 = low;
        s1L5 = 0;
        s1CC = 0;#threeUpLook( s1L1[1],  s1L2[1], s1L3[1], wave4Factor, AbsValue(s1L3[1] - s1L2[1])).offset_5;
    }
case threeDn:
#    if !downLook( s1L2[1]) {
    if threeDnOneUpLook(s1L1[1], s1L2[1], s1L3[1]){
        s1state = s1state.oneUp;
        s1org = Min(s1L3[1], low);
        s1L1 = high;
        s1L2 = 0;
        s1L3 = 0;
        s1L4 = 0;
        s1L5 = 0;
        s1CC=3;
#        s1CC = threeDnOneUpLook(s1L1[1], s1L2[1], s1L3[1]).level_4;
    } else if threeDnLook( s1L1[1],  s1L2[1],  s1L3[1],  wave4Factor, AbsValue(s1L3[1] - s1L2[1])) {
        s1state = s1state.threeDn;
        s1org = s1org[1];
        s1L1 = s1L1[1];
        s1L2 = s1L2[1];
        s1L3 = Min(s1L3[1], low);
        s1L4 = 0;
        s1L5 = 0;
        s1CC = 0;
#        s1CC=threeDnOneUpLook(s1L1[1], s1L2[1], s1L3[1]);
    } else { #w3>w1 and low>low[1]
        s1state = s1state.fourUp;
        s1org = s1org[1];
        s1L1 = s1L1[1];
        s1L2 = s1L2[1];
        s1L3 = s1L3[1];
        s1L4 = high;
        s1L5 = 0;
        s1CC = 0 ;
    }
 #end case threeDn: 


case fourUp:

    if high > s1L1[1] and high - s1L1[1] >= AbsValue(s1L1[1] - s1org[1]) * wave4Overlap {
        s1state = s1state.oneUp;
        s1org = Min(s1L3[1], low);
        s1L1 = high;
        s1L2 = 0;
        s1L3 = 0;
        s1L4 = 0;
        s1L5 = 0;
        s1CC = 4;

    } else if low >= s1L3[1] {
        s1state = s1state.fourUp;
        s1org = s1org[1];
        s1L1 = s1L1[1];
        s1L2 = s1L2[1];
        s1L3 = s1L3[1];
        s1L4 = Max(s1L4[1], high);
        s1L5 = 0;
        s1CC = 0;

    } else { #low < s1L3[1] 
        s1state = s1state.fiveDn;
        s1org = s1org[1];
        s1L1 = s1L1[1];
        s1L2 = s1L2[1];
        s1L3 = s1L3[1];
        s1L4 = s1L4[1];
        s1L5 = low;
        s1CC = 5;

    }
#end case fourUp:

case fourDn:
    if low < s1L1[1] and s1L1[1] - low >= AbsValue(s1L1[1] - s1org[1]) * wave4Overlap  {
        s1state = s1state.oneDn;
        s1org = Max(s1L3[1], high);
        s1L1 = low;
        s1L2 = 0;
        s1L3 = 0;
        s1L4 = 0;
        s1L5 = 0;
        s1CC = 4;

    } else if high <= s1L3[1] {
        s1state = s1state.fourDn;
        s1org = s1org[1];
        s1L1 = s1L1[1];
        s1L2 = s1L2[1];
        s1L3 = s1L3[1];
        s1L4 = Min(s1L4[1], low);
        s1L5 = 0;
        s1CC = 0;

    } else { # high > s1L3[1] 
        s1state = s1state.fiveUp;
        s1org = s1org[1];
        s1L1 = s1L1[1];
        s1L2 = s1L2[1];
        s1L3 = s1L3[1];
        s1L4 = s1L4[1]  ;
        s1L5 = high;
        s1CC = 5;

    }
#end case fourDn:
case fiveUp:

    if fiveUpLook(s1L3[1], s1L4[1], s1L5[1]) {
        s1state = s1state.fiveUp;
        s1org = s1org[1];
        s1L1 = s1L1[1];
        s1L2 = s1L2[1];
        s1L3 = s1L3[1];
        s1L4 = s1L4[1];
        s1L5 = Max(s1L5[1], high);
        s1CC = 5;#fiveUpLook(s1L3[1], s1L4[1], s1L5[1]).scan5up;

    } else {
        s1state = s1state.oneDn;
        s1org = Max(s1L5[1], high);
        s1L1 = low;
        s1L2 = 0;
        s1L3 = 0;
        s1L4 = 0;
        s1L5 = 0;
        s1CC = 5;#fiveUpLook(s1L3[1], s1L4[1], s1L5[1]).scan5up;

    }
case fiveDn:

    if fiveDnLook(s1L3[1], s1L4[1], s1L5[1]) {
        s1state = s1state.fiveDn;
        s1org = s1org[1];
        s1L1 = s1L1[1];
        s1L2 = s1L2[1];
        s1L3 = s1L3[1];
        s1L4 = s1L4[1];
        s1L5 = Min(s1L5[1], low);
        s1CC = 5;

    } else {
        s1state = s1state.oneUp;
        s1org = Min(s1L5[1], low);
        s1L1 = high;
        s1L2 = 0;
        s1L3 = 0;
        s1L4 = 0;
        s1L5 = 0;
        s1CC = 5;

    }
  #end case fiveDn:



}

#########################################################################
#########################################################################


plot org = if s1org and !IsNaN(close) then s1org else Double.NaN;
org.SetPaintingStrategy(PaintingStrategy.TRIANGLES);
org.SetHiding(!diagnostics);

def levelOneFix = CompoundValue(1,
    if s1state == s1state.oneDn and s1state[1] != s1state.oneDn then low
    else if s1state == s1state.oneUp and s1state[1] != s1state.oneUp then high
    else if s1state == s1state.oneDn then Min(low, levelOneFix[1])
    else if s1state == s1state.oneUp then Max(high, levelOneFix[1])
   else levelOneFix[1], 0);
plot one = if levelOneFix and !IsNaN(close) then levelOneFix else Double.NaN;
one.SetPaintingStrategy(PaintingStrategy.TRIANGLES);
one.SetHiding(!diagnostics);

plot two = if s1L2 and !IsNaN(close) then s1L2 else Double.NaN;
two.SetPaintingStrategy(PaintingStrategy.TRIANGLES);
two.SetHiding(!diagnostics);

plot three = if s1L3 and !IsNaN(close) then s1L3 else Double.NaN;
three.SetPaintingStrategy(PaintingStrategy.TRIANGLES);
three.SetHiding(!diagnostics);

plot four = if s1L4 and !IsNaN(close) then s1L4 else Double.NaN;
four.SetPaintingStrategy(PaintingStrategy.TRIANGLES);
four.SetHiding(!diagnostics);

plot five = if s1L5 and !IsNaN(close) then s1L5 else Double.NaN;
five.SetPaintingStrategy(PaintingStrategy.TRIANGLES);
five.SetHiding(!diagnostics);

plot st = if !IsNaN(close) then Floor(LowestAll(low) / 10) * 10 + s1state else Double.NaN;
st.SetHiding(!diagnostics);
def showStateBubbles = 1;

AddChartBubble((st != st[1] or BarNumber() == 1) && showStateBubbles && diagnostics, st,
if s1state == s1state.init then "0"
else if s1state == s1state.oneUp then "+1"
else if s1state == s1state.oneDn then "-1"
else if s1state == s1state.twoUp then "+2"
else if s1state == s1state.twoDn then "-2"
else if s1state == s1state.threeUp then "+3"
else if s1state == s1state.threeDn then "-3"
else if s1state == s1state.fourUp then "+4"
else if s1state == s1state.fourDn then "-4"
else if s1state == s1state.fiveUp then "+5"
else if s1state == s1state.fiveDn then "-5"
else "?", Color.GRAY);

def refLevel =
    if s1state == s1state.oneUp or s1state == s1state.oneDn then levelOneFix
    else if s1state == s1state.twoUp or s1state == s1state.twoDn then s1L2 
    else if s1state == s1state.threeUp or s1state == s1state.threeDn then s1L3
    else if s1state == s1state.fourUp or s1state == s1state.fourDn then s1L4 
    else if s1state == s1state.fiveUp or s1state == s1state.fiveDn then s1L5 
    else 0;
plot ref = if refLevel then refLevel else Double.NaN;
ref.SetHiding(!diagnostics);

def bn = CompoundValue(1, bn[1] + 1, 1);
def s = s1state;
def waveCnt = s1CC % 100;
def upState = s1state == s1state.oneUp or s1state == s1state.twoUp or s1state == s1state.threeUp or s1state == s1state.fourUp or s1state == s1state.fiveUp;

def noLabelState = (s == 3 or s == 4 or s == 7 or s == 8) and (
    fold n = 1 to 1000 with nn while !Floor(nn / 10) do 
        if GetValue(s, -n) == s then 0 
        else if GetValue(s, -n) != 1 and GetValue(s, -n) != 2 then 10 
        else 11
) % 10;  

#plot nls=nolabelState ;

def labelPt =
    if s1state == s1state.init then 0
    else if !s1org then 0
    else if noLabelState then 0
    else if formingBar and upState then high == refLevel
    else if formingBar then low == refLevel
    else if upState then
         ((high[-1] crosses below refLevel or (refLevel[1] < refLevel && refLevel > refLevel[-1])) and high == refLevel 
        and !(fold k = 1 to 1000 with kk while !IsNaN(GetValue(close, -k)) and GetValue(s, -k) == s && !kk do refLevel < GetValue(refLevel, -k) or GetValue(high, -k) == refLevel))

    else
        ((low[-1] crosses above refLevel or (refLevel[1] > refLevel && refLevel < refLevel[-1])) and low == refLevel 
        and !(fold m = 1 to 1000 with mm while !IsNaN(GetValue(close, -m)) and GetValue(s, -m) == s && !mm do refLevel > GetValue(refLevel, -m) or GetValue(low, -m) == refLevel))

;

DefineGlobalColor("Motive", Color.whiTE);
DefineGlobalColor("Corrective", Color.DOWNTICK);

def newWave = ( s1state == s1state.oneUp and s1state[1] != s1state.oneUp) or ( s1state == s1state.oneDn and s1state[1] != s1state.oneDn);
def fail = if newWave then fold a = 1 to 1000 with aa while !aa do GetValue(waveCnt, -a) else fail[1];

AddChartBubble( 
    labelPt and fail == 5
    , refLevel 
    , text =
    if s1state == s1state.oneUp or s1state == s1state.oneDn then if fail == 5 then "1" else "A"
    else if s1state == s1state.twoUp or s1state == s1state.twoDn then if fail == 5 then "2" else "B"
    else if s1state == s1state.threeUp or s1state == s1state.threeDn then if fail == 5 then "3" else "C"
    else if s1state == s1state.fourUp or s1state == s1state.fourDn then if fail == 5 then "SEND" else "D"
    else if s1state == s1state.fiveUp or s1state == s1state.fiveDn then "5"
    else "0"
    , color = if fail == 5 then GlobalColor("Motive") else GlobalColor("Corrective")
    , s1state == s1state.oneUp or s1state == s1state.twoUp or s1state == s1state.threeUp or s1state == s1state.fourUp or s1state == s1state.fiveUp
);
def HideEm = 1;
plot BullTrigger = s1state == s1state.fourUP and fail == 5 and labelPt;
plot BearTrigger = s1state == s1state.fourDn and fail == 5 and labelPt;
BullTrigger.SetHiding(HideEm == 1);
BearTrigger.SetHiding(HideEm == 1);

def rule1 = AbsValue(five - four) < AbsValue(three - two);
def w1w3 = Round(AbsValue(one - org) / AbsValue(three - two));
def w2w1 = Round(AbsValue(two - one) / AbsValue(one - org));
def w4w3 = Round(AbsValue(four - three) / AbsValue(three - two));
def w5w3 = Round(AbsValue(five - four) / AbsValue(three - two));
AddChartBubble(
(s1state == s1state.fiveDn or s1state == s1state.fiveUp) and labelPt and summaries
, refLevel
, "w1/3=" + w1w3 + "\nw2/1=" + w2w1 + "\nw4/3=" + w4w3 + "\nw5/3=" + w5w3
, up = s1state == s1state.fiveUp
, color = GlobalColor("Motive")
);

plot hiMa = SimpleMovingAvg(price = high, length = 6, displace = -4);
hiMa.SetDefaultColor(Color.BLUE);
plot loMa = SimpleMovingAvg(price = low, length = 6, displace = -4);
loMa.SetDefaultColor(Color.DOWNTICK);

def fib0 =
        if fail != 5 then 0
        else if s1L3 and !s1L3[1] then
            fold b = 0 to 1000 with bb while !bb do if GetValue(labelPt, -b) then GetValue(s1L3, -b) else 0
        else if three and !(s1state == s1state.fiveUp or s1state == s1state.fiveDn) then fib0[1]
        else 0;

DefineGlobalColor("High Probability", Color.lIGHT_GREEN);
DefineGlobalColor("Medium Probability", Color.YELLOW);
DefineGlobalColor("Lowest Tradable Probability", Color.RED);

plot fib25 = if fib0 then (s1L2 - fib0) * 0.25 + fib0 else Double.NaN;
fib25.SetDefaultColor(GlobalColor("High Probability"));
plot fib434 = if fib0 then (s1L2 - fib0) * 0.434 + fib0 else Double.NaN;
fib434.SetDefaultColor(GlobalColor("Medium Probability"));
plot fib618 = if fib0 then (s1L2 - fib0) * 0.618 + fib0 else Double.NaN;
fib618.SetDefaultColor(Color.DOWNTICK);

AddCloud(fib25, fib434, GlobalColor("High Probability"), GlobalColor("High Probability"));
#AddCloud(fib434, fib618, GlobalColor("Lowest Tradable Probability"), GlobalColor("Lowest Tradable Probability"));

##########################################
#   AddChartBubble(barnumber()==132, st, "cc=" + s1CC);
###############################
