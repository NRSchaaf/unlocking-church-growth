# Features Analyzed in the Church Growth Analysis

## Change

### change_increase

 - Description: This is an engineered feature indicating if a congregation reported an increase of less than or more than 10%.
 - change_increase = "Increased less than 10 percent" + "Increased more than 10 percent"

### change_decrease

 - Description: This is an engineered feature indicating if a congregation reported an decrease of less than or more than 10%.
 - change_decrease = "Decreased less than 10 percent" + "Decreased more than 10 percent"

## Facilities

### BLDGTYPE

- **Type of Building (BLDGTYPE)**
  - Description: Indicates the type of building that the congregation currently uses for primary worship services.
  - Includes:
    - School
    - Storefront
    - Church, synagogue, temple or mosque
    - Other

### VIEWBLDG

- **Vistors View the Building (VIEWBLDG)**
  - Description: Indicates if vistitors ever come to view the building or worship space to look at its architecture, artwork, stained glass, or statues.
  - Boolean

### REMODEL

- **Recent Major Remodeling (REMODEL)**
  - Description: Indicates if the congregation had done a recent, major remodel or construction project of the building(s).
  - Boolean

### BLDGYEAR

- **Age of Building (BLDGYEAR)**
  - Description: The year the primary building was constructed.
  - Date

### HOMESCHL

- **Home School Support (HOMESCHL)**
  - Description: Indicates if the congregation provides materials, programs, or activities specifically for home-school groups.
  - Boolean

### HAVESCHL

- **Have a School (HAVESCHL)**
  - Description: Indicates if the congregation has an elementary, middle and/or high school (K-12).
  - Boolean

### USEBLDG

- **Use of Building (USEBLDG)**
  - Description: Indicates if there have been groups, programs, or events that have no connection to the congregation that have used or rented space in the buildings.
  - Boolean

### PERMPURP

- **Purpose of Permits/Licenses (PERMPURP)**
  - Description: Indicates the purpose for which a congregation sought permits or licenses, if applicable.
  - Remarks: This item was recorded only if a congregation reported trying to obtain a permit or license (PERMIT=1).
  - Examples of purposes:
    - Kitchen
    - Building/Remodeling
    - Liquor License
    - Day Care License
    - Bingo/Gambling/Raffle License
    - Signage/Statue
    - Festival/Bazaar
    - Zoning
    - Tax Exemption
    - etc.

## Music

### SINGING

- **Singing by Congregation (SINGING)**
  - Description: Indicates there was singing by the congregation during the service.
  - Boolean

### CHOIR

- **Singing by Choir (CHOIR)**
  - Description: Indicates there was singing by a choir during the service.
  - Boolean

### PIANO

- **Piano Music (PIANO)**
  - Description: Indicates there was a piano used during the service.
  - Boolean

### ORGAN

- **Organ Music (ORGAN)**
  - Description: Indicates there was an organ used during the service.
  - Boolean

### DRUMS

- **Drum Music (DRUMS)**
  - Description: Indicates there were drums used during the service.
  - Boolean

### ELECGTR

- **Electric Guitar Music (ELECGTR)**
  - Description: Indicates there was an electric guitar used during the service.
  - Boolean

### GUITAR

- **Guitar Music (GUITAR)**
  - Description: Indicates there was a guitar used during the service.
  - Boolean

## Staffing

Note that the Staffing Analysis does not include analysis of a full-time lead or head clergy member as this is assumed applicable to all congregations.

### FTSTAFF

- **Full-Time Childrens Ministry (FTSTAFF)**
  - Description: Indicates how many full-time employees there are.
  - integer
 
### PTSTAFF

- **Part-Time Childrens Ministry (PTSTAFF)**
  - Description: Indicates how many part-time employees there are.
  - integer

### FTSCHLD

- **Full-Time Childrens Ministry (FTSCHLD)**
  - Description: Indicates how many full-time children's ministry employees there are.
  - integer
 
### PTSCHLD

- **Part-Time Childrens Ministry (PTSCHLD)**
  - Description: Indicates how many part-time children's ministry employees there are.
  - integer

### FTSYOUTH

- **Full-Time Youth Ministry (FTSYOUTH)**
  - Description: Indicates how many full-time youth ministry employees there are.
  - integer

### PTSYOUTH

- **Part-Time Youth Ministry (PTSYOUTH)**
  - Description: Indicates how many part-time youth ministry employees there are.
  - integer

### FTSYA

- **Full-Time Young Adult Ministry (FTSYA)**
  - Description: Indicates how many full-time young adult ministry employees there are.
  - integer

### PTSYA

- **Part-Time Young Adult Ministry (PTSYA)**
  - Description: Indicates how many part-time young adult ministry employees there are.
  - integer

### FTSMUSIC

- **Full-Time Music Ministry (FTSMUSIC)**
  - Description: Indicates how many full-time music employees there are.
  - integer

### PTSMUSIC

- **Part-Time Music Ministry (PTSMUSIC)**
  - Description: Indicates how many part-time music employees there are.
  - integer

### FTSREDU

- **Full-Time Religious Education (FTSREDU)**
  - Description: Indicates how many full-time religous education employees there are.
  - integer

### PTSREDU

- **Part-Time Religious Education (PTSREDU)**
  - Description: Indicates how many part-time religious eduation employees there are.
  - integer

### FTSFAMIN

- **Full-Time Religious Education (FTSFAMIN)**
  - Description: Indicates how many full-time family ministry employees there are.
  - integer

### PTSFAMIN

- **Part-Time Religious Education (PTSFAMIN)**
  - Description: Indicates how many part-time family ministry employees there are.
  - integer

### FTSCARE

- **Full-Time Pastoral Care (FTSCARE)**
  - Description: Indicates how many full-time pastoral care employees there are.
  - integer

### PTSCARE

- **Part-Time Pastoral Care (PTSCARE)**
  - Description: Indicates how many part-time pastoral care employees there are.
  - integer

### FTSPSYCH

- **Full-Time Psychological Counseling (FTSPSYCH)**
  - Description: Indicates how many full-time psychological counseling employees there are.
  - integer

### PTSPSYCH

- **Part-Time Psychological Counseling (PTSPSYCH)**
  - Description: Indicates how many part-time psychological counseling employees there are.
  - integer

### FTSENGAG

- **Full-Time Community Engagement (FTSENGAG)**
  - Description: Indicates how many full-time community engagement employees there are.
  - integer

### PTSENGAG

- **Part-Time Community Engagement (PTSENGAG)**
  - Description: Indicates how many part-time community engagement employees there are.
  - integer

### FTSENGAG

- **Full-Time Community Engagement (FTSENGAG)**
  - Description: Indicates how many full-time community engagement employees there are.
  - integer

### PTSENGAG

- **Part-Time Community Engagement (PTSENGAG)**
  - Description: Indicates how many part-time community engagement employees there are.
  - integer

### FTSGROW

- **Full-Time Spiritual Growth (FTSGROW)**
  - Description: Indicates how many full-time spiritual growth employees there are.
  - integer

### PTSGROW

- **Part-Time Spiritual Growth (PTSGROW)**
  - Description: Indicates how many part-time spiritual growth employees there are.
  - integer

### FTSREACH

- **Full-Time Outreach (FTSREACH)**
  - Description: Indicates how many full-time outreach employees there are.
  - integer

### PTSREACH

- **Part-Time Outreach (PTSREACH)**
  - Description: Indicates how many part-time outreach employees there are.
  - integer

### FTSADMIN

- **Full-Time Administration (FTSADMIN)**
  - Description: Indicates how many full-time administration employees there are.
  - integer

### PTSADMIN

- **Part-Time Administration (PTSADMIN)**
  - Description: Indicates how many part-time administration employees there are.
  - integer

### FTSVOLC

- **Full-Time Volunteer Coordinator (FTSVOLC)**
  - Description: Indicates how many full-time volunteer coordinator employees there are.
  - integer

### PTSVOLC

- **Part-Time Volunteer Coordinator (PTSVOLC)**
  - Description: Indicates how many part-time volunteer coordinator employees there are.
  - integer

### FTSWTECH

- **Full-Time Worship-Related Technology (FTSWTECH)**
  - Description: Indicates how many full-time worship-related technology employees there are.
  - integer

### PTSWTECH

- **Part-Time Worship-Related Technology (PTSWTECH)**
  - Description: Indicates how many part-time worship-related technology employees there are.
  - integer

### FTSTECH

- **Full-Time Technology Other Than Worship (FTSTECH)**
  - Description: Indicates how many full-time technology other than worship-related employees there are.
  - integer

### PTSTECH

- **Part-Time Technology Other Than Worship (PTSTECH)**
  - Description: Indicates how many part-time technology other than worship-related employees there are.
  - integer

### FTSMEDIA

- **Full-Time Media (FTSMEDIA)**
  - Description: Indicates how many full-time media employees there are.
  - integer

### PTSMEDIA

- **Part-Time Media (PTSMEDIA)**
  - Description: Indicates how many part-time media employees there are.
  - integer

## Worship

### NUMSERV1

- **Services per Week (NUMSERV1)**
  - Description: Indicates how services per week there are.
  - integer

### LENGTH

- **Length of Service (LENGTH)**
  - Description: Indicates how long did the last servcie last.
  - integer

### SERMON

- **Had Sermon (SERMON)**
  - Description: Indicates if there was a sermon as part of the service.
  - Boolean

### SERMTIME

- **Sermon Time (SERMTIME)**
  - Description: Indicates how long the last sermon was.
  - integer

### SPKRDWN

- **Speaker Down from Stage (SPKRDWN)**
  - Description: Indicates if the speaker came down from the altar, podium, chancel, or stage during the sermon.
  - Boolean

### NUMSPOKE

- **Unique Speakers (NUMSPOKE)**
  - Description: Indicates the number of unique speakers during the last service.
  - integer

### GREET

- **Congregation Greeting During Service (GREET)**
  - Description: Indicates if there was a time for congregational greetings, hand shaking, etc. during the last service.
  - Boolean

### KIDTIME

- **Part Specifically for Children (KIDTIME)**
  - Description: Indicates if there was a part of the service specifically directed at children.
  - Boolean

### TEENPART

- **Part Specifically for Teens (TEENPART)**
  - Description: Indicates if any teens participated by speaking, singing, or performing during the service, not including in the choir or general congregation.
  - Boolean

### ROBE

- **Leader in Robe (ROBE)**
  - Description: Indicates if the clergy leader wore a robe.
  - Boolean

### APPLAUSE

- **Applause (APPLAUSE)**
  - Description: Indicates if there was an applause at any point in the service.
  - Boolean

### LAUGH

- **Laughing (LAUGH)**
  - Description: Indicates if there was any laughing at any point in the service.
  - Boolean

### PROGRAM

- **Program or Bulletin (PROGRAM)**
  - Description: Indicates if a program, bulletin or other written order of service were handed out for people to follow.
  - Boolean

### OVERHEAD

- **Overhead Projector or Screen (OVERHEAD)**
  - Description: Indicates if visual projection equipment was used.
  - Boolean

### STREAMED

- **Streamed (STREAMED)**
  - Description: Indicates if the service was broadcast or streamed live so that people outside the building or campus could see it.
  - Boolean

### STMPHONE

- **Smart Phone (STMPHONE)**
  - Description: Indicates if people were offered the opportunity to use their smartphones during the service to participate in some way.
  - Boolean

### CONGREAD

- **Congregational Reading (CONGREAD)**
  - Description: Indicates if the congregation spoke, read, or recited something together at any point.
  - Boolean

### OFFERING

- **Monetary Offering (OFFERING)**
  - Description: Indicates if a monetary offering was collected during the service.
  - Boolean

### SOCLTIME

- **Social Time (SOCLTIME)**
  - Description: Indicates how long people usually mingle and socialize informally with each other before and after the service (in minutes).
  - integer

## Programs

### CLSYACS

- **College/Young Adult Religious Education Classes (CLSYACS)**
  - Description: Indicates if religious classes for young adults or college students are offered at least weekly.
  - Boolean

### CLSADLT

- **Adult Religious Education Classes (CLSADLT)**
  - Description: Indicates if religious classes adults of any age are offered at least weekly.
  - Boolean

### YTHGRP

- **Youth Group for Teens (YTHGRP)**
  - Description: Indicates if there is an organized youth group for teenagers.
  - Boolean

### TEENCHOR

- **Choir for Teens (TEENCHOR)**
  - Description: Indicates if there are choirs or other musical groups composed primarily of teenagers.
  - Boolean

### TEENCAMP

- **Teen Camps (TEENCAMP)**
  - Description: Indicates an annual participation in youth retreats, conferences, or camps.
  - Boolean

### TEENVOL

- **Teen Volunteer Projects (TEENVOL)**
  - Description: Indicates teens have participated in service projects or volunteer projects through the congregation.
  - Boolean

### POLITICS

- **Discuss Politics (POLITICS)**
  - Description: Indicates any meetings, groups, or classes specifically focused on discussing politics.
  - Boolean

### DISBIBLE

- **Bible Class (DISBIBLE)**
  - Description: Indicates any meetings, groups, or classes specifically focused on discussing the bible.
  - Boolean

### BOOKS

- **Books Class other than Bible (BOOKS)**
  - Description: Indicates any meetings, groups, or classes specifically focused on discussing books other than the bible.
  - Boolean

### PARENTS

- **Parents Class (PARENTS)**
  - Description: Indicates any meetings, groups, or classes specifically focused on discussing parenting.
  - Boolean

### VOTERREG

- **Voter Registration Meetings (VOTERREG)**
  - Description: Indicates any meetings, groups, or classes specifically focused on an effort to get people registered to vote.
  - Boolean

### SCIENCE

- **Science & Religion (SCIENCE)**
  - Description: Indicates any meetings, groups, or classes specifically to discuss any sort of scientific issue or the relationship between science and religion.
  - Boolean

### ENVIRON

- **The Environment (ENVIRON)**
  - Description: Indicates any meetings, groups, or classes specifically to discuss issues related to the environment.
  - Boolean

### ORGVOLS

- **Volunteer Group (ORGVOLS)**
  - Description: Indicates any meetings, groups, or classes specifically to organize or encourage people to do volunteer work.
  - Boolean

### WORKPROB

- **Concerns at Work Group (WORKPROB)**
  - Description: Indicates any meetings, groups, or classes specifically to discuss people's problems or concerns at work.
  - Boolean

### NEWMEMS

- **New Members (NEWMEMS)**
  - Description: Indicates any meetings, groups, or classes specifically focused on prospective or new members.
  - Boolean

### TRAIN

- **Religious Education Training (TRAIN)**
  - Description: Indicates any meetings, groups, or classes specifically focused on training new religious education teachers.
  - Boolean

### RACEREL

- **Race & Race Relations (RACEREL)**
  - Description: Indicates any meetings, groups, or classes specifically to discuss issues related to race and race relations.
  - Boolean

### OTHTRAD

- **Other Religions (OTHTRAD)**
  - Description: Indicates any meetings, groups, or classes specifically to discuss or learn about religions other than your own.
  - Boolean

### OWNMONY

- **Personal Finances (OWNMONY)**
  - Description: Indicates any meetings, groups, or classes specifically to discuss or learn how to manage one's personal finances.
  - Boolean

### CONGMONY

- **Congregation Finances (CONGMONY)**
  - Description: Indicates any meetings, groups, or classes specifically to discuss how to improve the management of your congregation's finances.
  - Boolean

### ASSESS

- **Community Assessment (ASSESS)**
  - Description: Indicates any meetings, groups, or classes specifically to plan or conduct an assessment of community needs.
  - Boolean

### MARRIAGE

- **Marriage Enrichment (MARRIAGE)**
  - Description: Indicates any meetings, groups, or classes specifically for married couples on enriching or improving their marriage.
  - Boolean

### WOMENGRP

- **Women's Group (WOMENGRP)**
  - Description: Indicates any meetings, groups, or classes specifically for women.
  - Boolean

### MENGRP

- **Men's Group (MENGRP)**
  - Description: Indicates any meetings, groups, or classes specifically for men.
  - Boolean

### EXERCISE

- **Exercise Class (EXERCISE)**
  - Description: Indicates any meetings, groups, or classes specifically focused on exercise or promoting physical activity.
  - Boolean

### LGBT

- **LGBTQ Group (LGBT)**
  - Description: Indicates any meetings, groups, or classes specifically focused on discussing issues related to sexual orientation or gender identity.
  - Boolean
