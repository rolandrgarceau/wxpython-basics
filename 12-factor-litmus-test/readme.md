# 12 Factor App Litmus test with a Well-Architected Framework

## The entire reworking of whitepapers here is from the perspective of diagnostics and consultation. 
When preparing for a project design meeting there are considerations to be had. This particular overview integrates the 12 factor app methodology with AWS 5 Pillars, and a fair deal of team participation at the entry level with learn-it-the-hard-way top down dictation from not so intuitive leadership as the papers seek to guide us on.

Rules aren't meant to be broken, but are surely meant for the bending, right- especially the ones we had in our binders at school. Learning to build applications start with the basics, moving to more complex portions that encompass robust solutions. Defining "the" system for a customer is no easy process, and can be quite challenging for small startups. Pulling from all your available resources to create an unique perspective is what people really wish to see when attempting to fill a void within an organization, and we as the solution providers often have to tiptoe at suggestions that are out of the box, innovative, and a brilliant addition to the original collective thought for a system while the plan can be devised, put on paper, and researched enough to play the politics of convincing others on the team that this is the way the ship needs to sail. In the mean time hold the ropes down tight and enjoy the ride.

When you find yourself suddenly becoming the newfound "expert" of someone elses latest and greatest idea, often the road may be rocky to say the least- especially if they are expecting that you learn their system and employ their tooling to complete their list of requirements, even if you are transparent and honest about your skill-set and requirements needed to meeting theirs. Often to find robust alternative thought on a subject requires outside view of a system, and this can yield introspect to the validity of design at play, down to the very fundamental level of reworking planning and development strategies to suit, not only from a 1-10 person team, but all the way up through organizations employing thousands.

Showing utility to having a need for any type of service outside of the unknown unknowns to aid the business requires a well thought out plan and execution strategy, so this portion will attempt to ligitimize some technologies white papers for potential adaptation within any proposal. Few wish to admit utility to that, nor like to submit to paying for the development of alternatives to their greatest idea- it's just that- *their* greatest idea, not yours. Sometimes being really good at delivering this kind of solution means leaving certain aspects of an optimal offering out of those board meetings at the infancy of the project, with the intent of getting back to the important parts after trust is established and the foundation is laid out well enough for every entity involved to comprehend what the vision, direction, and individual motivations are that are steering and guiding progress to a commonly agreed upon goal. Sometimes just getting through the door isn't so easy either.

This means we as developers may have to find clever ways at getting paid to be a "Consultant", establish a trust and validity to reasoning and suggesting features that may not even be exposed in the first place, for the simple sake of doing the right thing, and sometimes at the cost of jeopardizing your accreditation in doing so. Then be able to work the model that presses the entire package to the next level one byte at a time. Some people think they know all they need about a subject and don't want to hear someone with less of a degree with good ideas. Some don't want "help" offered to them, some don't have room to ingest anything outside of their own blinders on a subject matter. A KISS is not always as simple as it seems, sometimes it is. Be careful here it may lead one looking for a job more than actually doing one.

Be very aware of situational environments as such, and have plans to avoid detrimental encounters in these different divergent pathways as they are presented. That will help keep progress moving forward, and with a paycheck in hand. It takes hours of testing the waters, employing NLP, breaking off ingestible chunks of information for people that may not be as insightful as your vision, may not be fully aware of what they want, and need someone (they might not have thought it would be you in the hiring process) to show them the gem before their own eyes. Making this a blend-able solution deeper than just the chameleon's skin for any of the above means merging well architected frameworks with every situation laid out before us, not only from a software perspective, but also from life's point of view. Being able to be keen to all the environmental noise is key. Life is definitely that box of chocolates melted upon the stack of Jacksons in their wallet. I'm a Jackson descendent myself.

Sometimes people on want the simple solution, nothing more. Sometimes catching onto that quick and doing something about it is a challenge in itself. That too has to be realized and not cryptically deciphered through the thought of all those so called transparent meetings we have to talk about the solution. Sometimes it is also as easy as cutting through all the what ifs and starting with the what nows. Sometimes there is no meeting necessary, just go out and do it.

## Well, Architect Something already

This takes time, like a fine merlot. AWS has 5 pillars to consider too when designing solutions. Jeffersonian pillars last centuries, code sadly often does not these days. For small business I like to take this down to a learning model for new technology and attempt to use the baby step hello worlds to build and understanding with for those that may not be as technically adept with the solutions that present themselves along the journey. Often it is the journey itself- along the path as it is chosen- that influences the walk taken to that destination address. For that we start with addressing some of the factors, a few of the pillar highlights, and mold the solution dependent of the walk that path takes us. Start with addressing points from the documentation for the [12 factor app](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=2ahUKEwiapP6zn4rlAhWqmuAKHTTUAFwQFjAAegQIABAB&url=https%3A%2F%2Fwww.12factor.net%2F&usg=AOvVaw29kcod8U04nG_IgZONQOCk) and [AWS 5 Pillars](https://aws.amazon.com/blogs/apn/the-5-pillars-of-the-aws-well-architected-framework/). 

In reality we may already have quite a bit of ground covered before we even hit this fork process- there may be months of unrefined thoughts and notes written down already. Then from here, if there is already significant understanding on the topics involved it becomes the dance of prioritization, filtering the content, filling gaps, and expanding on the points of interest matching requirements and features with wants and desires (while having some semblance of scope and boundaries established prior to moving along the path). This can often be seen as being hired to remodel a home (or build a new one) where your job at hire is to build it, then in realization of your potential the job scope becomes consultant, interior decorator, landscaper, painter, and coordinator (I personally buck on the choosing or even recommending the paint color). Trying to make all of that clear from the get go is less than a trivial task. The following dissection, however will help mitigate some of these concerns however:

## Codebase

* Tracked in a version control system, such as Git, Mercurial, or Subversion repository
  * App-single code base vs. Distributed system for multiple branches
  * It is all distributed today. But can we add in one offs for every customer? Simple Config the config.
    * less trouble ticketing happening
    * less time spent from developer support
    * happier end user
* How do we manage it all?
  * design the design? Containerize a container? Where does it end?
* Deploy all the one offs the same exact way, every time, a direct conflict of 12 factors?
  * maybe we argue this means we are just making an application then, with hopes that one day it becomes distributed... dream on.

We can get down to the Burger King mentality right here and now. Have it your way. Make an "App", or make an account for your customer- each end every one of them. Give them their own customize-able feature-set with a minimal input configuration. Wait a minute what did you just say? We are going to have to create and pay for every single user on our system just so that we can suit their ever-lasting want and desire? Really? That just costs too much they say. Well, it all depends on how well you wish to pass UX. Design for that in mind. See the Litmus test below for more details.

How many licks does it take to get to the center of a tootsie roll pop? Don't think lick here, think bytes- one at a time. how many clicks does it take to check out? What is the purpose of the impulse isle, and does that suit the 3 click to a credit card submission request? If not we may need to look back at the design. Waterfalled too much at the beginning or agilely know we are going to switch things around anyway so don't get too stuck at the beginning? 

## Dependencies

Two parts not to be messed with:

* dependency declaration manifest
* dependency isolation 

One very gray area: 

We need simplified developer setup with a simplified build command. The problem lays in the hundreds of frameworks and tooling suites developers are expected to know- each having their "simplified" cli. If the round table that sits to design Dev is not also Ops this can lead way down the path to the dark side. Too hard to implement some of the aforementioned caveats- with sentiment leading to the lack of faith in their staff or employee training.

In python Pip is used for declaration and Virtualenv for isolation. These are separate tools. Ruby has a gemfile manifest for declaration and bundle exec for dependency isolation. C has autoconf.

### Gotchas on Deps

Watch the system tools having to be included with the system calls. Platform agnostic we say? Well put the tools in the bag and not worry about it having to be dealt with by an administrator. Evertything there to run the code- period- ships with the application. Now we gotta talk about Liscense, upstream support, and Legal notice- all of which comes with $$$ vs time vs in house resources.

## Config in the environment

Which one? Conda? Virtualenv? Shell? OS? Container. Container. Container. Trying not to vary staging environements from dev, prod, test, etc. means quite a bit different thing today. System integrity protection on a Mac is worthy of emulation. Python "v" words are not.

12 factor aims at *strict separation of config from code* so storing config as constants seems a violation here. When code stays the same and config changes across deploys, this may appear that on the surface that this means more human interaction if we do such things as having every user with their own configuration.

## Litmus test to separate env vars
According to the 12 factor app, this litmus is: Can the codebase be made open source at any moment, without compromising any credentials? This will tell you if the configuration would be correctly factored. This means the sensitive information is in the environment, but if the configuration gets checked in to version or revision control, that may be a compromised solution. Therefore we have a system specific to the deployment schedule specific for security, environmental, and config. 

In rails we can see internal application config in code with config/routes.rb or in Spring how code module connections transpire. Also in rails we can see config/database.yml. The yaml files have a few catches, however. If we accidentally check these into code repo there can be multiple versions of that config passed around or scattered to various locations, and even in different formats (JSON, and xml instead of just a plain yml or .spec) These formats can also be language specific or framework specific too.

So the config happens with environmental variables outside the code base to assist the process of variant deploys with the same code base. This also allows for our Burger King mentality mentioned above. Associated batched grouping for staged environments and deployment strategies may not address scaling effectively, as this requires additional naming of groups as expansion occurs. Managing deploys this way can create brittle infrastructure. The environmental variables may become the granular means to addressing such concerns, keeping in mind that they are never grouped together as "environments" but independently managed per deploy.

## Backing environments

Can be treated as attached resources, and all the code used for accessing them can be treated the same- no distinction between local or third party. In fact with containerized infrastructure they may also come up as such in the case for Docker and Kubernentes (attached network resources). These may be in the form of backing services across a network to include a MySQL DB, RabbitMQ or ZeroMQ, Beanstalkd, SMTP servies for email outbound traffic like Postfix or Postmark, and caching with memcached or redis. Not only would these all be treated as attached, we may further set the traditional DB infrastructure to a local containerized deploy with its own set of closer resources to the 12 factor app in question. Third party services may fall into place here for consumable CORS like integrations with things like Google maps or Twitter. All of the above can be called out with a config containing URL and access information.

Integration of external services should be seamless and easy to swap between- *without* having to modify code. this means only hav ing to swap the resource handle from within the config. Likewise if a DB is not performing properly, having them loosely coupled here also means a new DB can be spun up and reinstated from backup, and put into the production environment without any code change. We can see this in the kubernetes-wxpython section for deployment and how binaries will be generated through RPC and deployed to images for containers to delegate this within the backing infrastructure.

## Build, Release, ~Ruin~, I mean run:)

The code goes from zero to hero (dev to prod) in 3 Jedi, wave your wand in Diagon Alley steps:

1. Build: fetches the vendor dependencies and creates binaries and assets.
2. Release: takes the build and combines the deploys current config. This will allow the immediate use and execution within its released execution environment.
3. Run Stage: Runtime will actually be launching processes here in the execution environment against a selected release.

Abracadabra! We are jammin'. Now what? What happens when there's a problem? Auto rollback.

## Autorollback

Take a look at my code for the "serverless" Lambda function to complete all the above steps within AWS resources The code attempts to create the production release after being instigated from a hook coming from a git push and triggered by a S3 put operation into a particular bucket. This process will unwind itself if any part of the stages involved in the CodePipeline achieves undesired results (emitters from each CodeBuild and Code Deploy opt to use the except block and not the failed resource artifact)
```py
import json
import boto3
from botocore.client import Config
import StringIO
import io
import zipfile
import mimetypes


def lambda_handler(event, context):
    sns = boto3.resource('sns')
    topic = sns.Topic('arn:aws:sns:us-east-1:678674041111:deployPortfolioTopic')
    #we may wish to use codepipeline or our first hardcoded bucket to run this script
    #define the location here as the hardcoded one at first then overwrite if job: below
    #then update the original hardcoded calls for the buckets with the variable/dictionary keys insteadd
     #file name is what we may be thinking for objectKey
    location = {
        "bucketName": 'portfolio-build.rudy-garceau.info',
        "objectKey": 'portfolio-artifact.zip'
    }
    try:
        # get the codepipeline event object
        job = event.get("CodePipeline.job")
        #if not invoked by pipeline it wont be there, so manual invoke skips if job:
        if job:
            #dictionary keys match the event object example at
            #https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-invoke-lambda-function.html#actions-invoke-lambda-function-json-event-example
            #see inputArtifacts, look for name of artifact from code pipeline created bucket - look thru s3 BuildArtif is folder under
            #we had hardcoded bucketname and object key portfoilio.rudy-garceau.info and key portfolio-artifact.zip file at first
            for artifact in job["data"]["inputArtifacts"]:
                if artifact["name"] == "BuildArtif": #Robin's was myAppBuild
                    location = artifact["location"]["s3Location"]

        #to have log give the location of where the build is coming from
        print ("Lambda portfolio is building from" + str(location))
        
        #this may fix the --profile issue but check if lambda exe role needs other in memory perms....iobytes
        #configured profiles but aws configure list doesnt show the profile
        #session = boto3.Session(profile_name='portfolio-access-usr') # try: $ aws configure list
        #s3 = session.resource('s3', config=Config(signature_version='s3v4') )
        
        #it is possible to have to do aws kms encryp issues uncomment the next two lines comment other resouce call
        #from botocore.client import Config
        #s3 = boto3.resource('s3',config=Config(signature_version='s3v4'))
        #session = boto3.Session(profile_name='portfolio-access-usr')
        s3 = boto3.resource('s3')
        #s3 = session.resource('s3')
        portfolio_bucket = s3.Bucket('portfolio.rudy-garceau.info') 
        #build_bucket = s3.Bucket('portfolio-build.rudy-garceau.info') #original hardcoded to be used for unzipping
        build_bucket = s3.Bucket(location["bucketName"])
        # for obj in portfolio_bucket.objects.all():
        #     print obj.key
        # ipython didnt like no parenthesis
        #also dont need a print to upload unzipped files but its nice to see what youre working with
        # for obj in portfolio_bucket.objects.all():
        #     print (obj.key)
        #dont need to see the index, but you may want to check it later to see updates loaclly
        #portfolio_bucket.download_file('index.html', '/tmp/index.html')
        #dont need a local artifact
        #build_bucket.download_file('portfolio-artifact.zip', '/tmp/portfolio-artifact.zip')
        #import StringIO failed so we used io
        #this way we use everything in memory
        #zipped_code = StringIO.StringIO()
        zipped_code = io.BytesIO()
        #build_bucket.download_fileobj('portfolio-artifact.zip', zipped_code) #original hardcoded
        build_bucket.download_fileobj(location["objectKey"], zipped_code)
        #this prints the actual zipped content
        # with zipfile.ZipFile(zippped_code) as myzip:
        #     for nm in myzip.namelist():
        #         print (nm)
        with zipfile.ZipFile(zipped_code) as myzip:
            for nm in myzip.namelist():
                obj = myzip.open(nm)
                #portfolio_bucket.upload_fileobj(obj, nm) #upload as a file object, but changed for mimetypes
                portfolio_bucket.upload_fileobj(obj, nm, ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
                portfolio_bucket.Object(nm).Acl().put(ACL='public-read') #add the make public
        topic.publish(Subject="successful lambda portfolio deploy", Message=("success: portfolio deploy using "+str(location)))
        #the raw client was used for telling codepipeline that the lambda fcn was a success, and keep on....
        #we did not use the s3 = boto3.resource(config = Config....above commented out from botocore)
        if job:
            codepipeline = boto3.client('codepipeline')
            codepipeline.put_job_success_result(jobId=job["id"]) #from event object
    except:
        topic.publish(Subject="failed lambda portfolio deploy", Message=("failed: portfolio deploy using "+str(location)))    
        raise
    print ("portfolio extract and upload in lambda: job done")
    
    return {
        'statusCode': 200,
        'body': json.dumps('deployPortfolio has been run in Lambda')
    }
```
## Releases 

Having a tooling to save releases like Capistrano is good. We can also have a bucket with version number for regulation of releases, and to keep the changes as they are being built. this can also be used for artifactory management too.

## Processes

Part 6 of the 12 factor app is the broken down processes to run the app. For a standalone script we could be calling `python the-wxpython-standalone-app.py` or something similar from a local environment through a human entered cli command and flags. In reality we may have quite a bit of zero or more instances of a particular piece of software, all geared to handle load and at scale, all from their own associated base image. 

### 12 factor processes

Stateless processes and share nothing are the foundation here. The persistence is held through stateful backing services like a database. If the application is to exist at scale this makes management of static and dynamic data easier to deal with. 

### Persist ephemeral storage other than "Sticky Sessions"

But wxPython is a Gui framework. We are creating text files to hold csv data, why use a DB for a simple customer solution? Well, is it scalable? Does it need entrant locks and threads? Do we need to assert state and the 11 nines that AWS boasts? The memory space or filesystem of the process can be used as a brief, single-transaction cache. Remember a restart will often kill ephemeral stores and/or in memory or local file stores, so prepare for that by choosing a permanent persistent binding schema. See docker notes on declaring a "sharable" bind mount and Alpine lbu backup procedures for in depth descriptions on this.

Asset packagers like django-assetpackager use the filesystem as a cache for compiled assets. A twelve-factor app prefers to do this compiling during the build stage. Asset packagers such as the Jammit asset package manger for Rails and the Rails asset pipeline can be configured to package assets during the build stage.

Some web systems use “sticky sessions” which is caching user session data in memory of the app’s process and expecting future requests from the same visitor to be routed to the same process. This is *NOT* the way 12 factor works. It is UNRELIABLE. Session state information like this would be better dealt with in a DB with an expiry date in Redis or Memchached.

## Port Binding

PHP apps might run as a module inside Apache HTTPD, or Java apps might run inside Tomcat. For 12 factor apps it does not rely on runtime injection of a webserver into the execution environment to create a web-facing service. The web app exports HTTP as a service by binding to a port, and listening to requests coming in on that port. We see that in detail with the router-like execution of Kubernetes, as it exposes ports as needed to do such things. So does docker or any other LXC like implementation of containers. We just make most of this process easy with a local host and : port 5000 defined from within a URL. The bindings often come in the form of an aliased name and a router layer with the router handle. 

