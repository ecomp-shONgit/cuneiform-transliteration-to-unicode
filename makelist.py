# -*- coding: utf-8 -*-
import sys, string, time, codecs, os, unicodedata

#2012, eAqua Dissemination Project, Prof. Charlotte Schubert Alte Geschichte Leipzig
#Source list: http://de.wikipedia.org/wiki/Unicode-Block_Keilschrift
#Purpose: The program builds a CSV styled list with ";;" seperator to save the unicode, the name and the transliteration of cuneiform signs
#CSV: "count";;"unicodename";;"unicodenumber";;"translit"
#JS: first array transliteration to unicode, second list unicoden to html encoded signs

def makelistumschriftunicode( path, naming, javascriptarrayname, javascriptarrayname2 ):
    gf = open( path )
    gft = gf.read( )
    gf.close()
    
    htmltable = gft.split("<table")[ 1 ].split("</table>")[ 0 ].split("<tr>")
    
    out = ""
    outjavascriptarray = ""
    jsout2 = ""
    count = 1
    for i in xrange( len( htmltable ) ):
        if i > 0:
            count+=1
            unicodename = 'NULL'
            unicodenumber = 'NULL'
            umschrift = 'NULL'
            cuniformhtml = 'NULL'
            apart = htmltable[ i ].split("</td>")
            cuniformhtml = apart[ 1 ].split( 'class="cuneiform">' )[ 1 ]
            #print c
            unicodenumber = apart[ 0 ].split("+")[ 1 ].split(" (")[ 0 ]
            umschrift = apart[ 2 ].split("Keilschriftzeichen")[ 1 ]
            unicodename = apart[ 3 ].split("<small>")[ 1 ].split("</small>")[ 0 ]
            #print i, unicodename
            
            umschrift = "".join(umschrift.split()).decode('utf-8').lower().encode('utf-8')
            umschrift = "ḫ".join( umschrift.split("&nbsp;?") )
            umschrift = "ḫ".join( umschrift.split("?") )
            out = out + ( "%i;;%s;;%s;;%s\n" % (count, unicodename, unicodenumber, umschrift))
            outjavascriptarray = outjavascriptarray + javascriptarrayname +'["%s"] =  "\u%s";\n' % ( umschrift, unicodenumber )
            jsout2 = jsout2 + javascriptarrayname2 +'["\u%s"] =  "%s";\n' % ( unicodenumber,  cuniformhtml )

	    if("sub>2<" in umschrift):
                umword = umschrift.split( "<sub>2</sub>" )

                for h in xrange(0, len(umword), 2):
                    if(umword[ h ] == ""):
                        continue
                    letters = list( umword[ h ] )
                    lastletter = letters [ -1 ]
                    try:
                        letters [ len(letters)-1 ] = unicodedata.lookup( "LATIN SMALL LETTER %s WITH ACUTE" % ( lastletter.upper( ) )  ).encode("utf-8")
                    except:
                        letters [ len(letters)-1 ] = lastletter + unicodedata.lookup( "ACUTE ACCENT" ).encode("utf-8")
                        #print lastletter
                    umword[ h ] = "".join( letters )
                outjavascriptarray = outjavascriptarray + javascriptarrayname +'["%s"] =  "\u%s";\n' % ("".join(umword), unicodenumber )
                umschrift = "".join(umword)

	    if("sub>3<" in umschrift):
                umword = umschrift.split( "<sub>3</sub>" )

                for h in xrange(0, len(umword), 2):
                    if(umword[ h ] == ""):
                        continue
                    letters = list( umword[ h ] )
                    lastletter = letters [ -1 ]
                    try:
                        letters [ len(letters)-1 ] = unicodedata.lookup( "LATIN SMALL LETTER %s WITH GRAVE" % ( lastletter.upper( ) )  ).encode("utf-8")
                    except:
                        letters [ len(letters)-1 ] = lastletter + unicodedata.lookup( "GRAVE ACCENT" ).encode("utf-8")
                    umword[ h ] = "".join( letters )
                outjavascriptarray = outjavascriptarray + javascriptarrayname +'["%s"] =  "\u%s";\n' % ("".join(umword), unicodenumber )
    #print 
    outg = open( naming + ".csv", "w" )
    outg.write( out )
    outg.close( )
    outgjs = open( naming + ".js", "w" )
    outgjs.write( outjavascriptarray )
    outgjs.close( )
    outg2js = open( naming + "2.js", "w" )
    outg2js.write( jsout2 )
    outg2js.close( )

if __name__ == '__main__':
    print ( "On." )
    ##
    #Cuneiform / Keilschrift
    #fkt inp: input file name, outfilename1, outfilename2, outfilename3
    makelistumschriftunicode( "Unicode-Block_Keilschrift.html", "keilschrift", "akkadisch_um_keil", "akkadisch_keil_keilhtml")   
    print ( "Off." )

    
    
    
