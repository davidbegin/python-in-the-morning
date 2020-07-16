# 20202 - 7 - 14

## Today

- Learn some Go
- Figure out what I need to learn for GeoGuessr Game
  - Play the sounds
  - Read in Twitch Chat from IRC
  - Respond sound requests
  - Limit the amount people can play in a time period
  - CLI args

## What can I do Serverless Stuff

- Its NOT SERVERLESS -> it's servers on demand

You have no server running, and then when you make a request,
the cloud provider boots up micro-vm in Rust, serves your request,
and if no other request are coming it boots down.

You only pay when for when the server is up.
You have a website with no traffic.....then why pay for server stay

You have a cron-job that runs.....why not just boot a lambda for that one task?

You have Async process to take logs, format them and store them somewhere.
That doesn't need to respond to in real, throw it on a Lambda

What happens if you suddenly get a GIANT INFLUX of traffic,
You're cloud provider has to boot up lots of Lambdas,
and there is a speed penalty.

....there are also hard limits (in AWS).

You bootup time -> Boot it once and use for 30 mins, and then boot down.

Hyperready -> Real Name

Give me 3000 Lambdas now.
<https://aws.amazon.com/blogs/aws/new-provisioned-concurrency-for-lambda-functions/>

Cold Start -> Worst Case Scenario

Are you in a VPC
outside of VPC

What Code are you running on sTaRtUp.

50 -> 500ms

Cold Start Chaining Problems

## Yesterday

## Resources

<https://www.youtube.com/watch?v=dXidW7fEH8g>
link that to our ticketing system.

[90 Minutes of Focused Studying: The Best Binaural Beats](https://www.youtube.com/watch?v=eqKQACO4HAk)

## Bounties

## Viewer Questions

isaiahvander: how do you view it, then if not by motivation?

erikdotdev: expletif pick a small task first.
The quick win gets you going and
it's easier to keep up the momentum.
Looking at the entire task at once makes it
hard to even start.

Action Affects YOUR Emotions
If you start programming you will start feeling MORE "Motivated" to program

Motivatation Trap:

- Ohhh man this stream, youtube video, blog post, this person motivated me!!!
  I'm get work done!
  Look at all the work I did!

....Now I don't feel motivated anymore
....well I'm not going to work until I get that Motivation again.
    and thats a drug.

Make Schedule

nuke4fun: I think my real question is how do I do something without "motivation"

Make Panic/Sprial Routine:

Set a simple task that build to what I want I want:

(DONT GO LOOK FOR MOTIVATION)

- Journal about what I'm avoiding and what I want to get done -> 5-10 mins
- Meditate
- Clean My Apartment Up some
- Workout
- Walk
- Bike Ride
- Sit down at my computer, start at Pomodoro timing, and just work for those 25
  mins

......4 hours later still working.

I need to finish this TMUX Video
I suck at Shotcut

- I don't understand all the options I'm chosing, I keep messing somethign up,
  and not realizing what I need
- I need to just finish the intro and outro section

## Questions

## Learnings

## Ponderings

## Experiences

## Opinions

## Lifelong Goals

Eventually every part of my keyboard, should be from somewhere different,
each one, with J Peterman style story to accompany.

## Debates

## Confessions

## Quotes

## Scraps

## TODO

yatko: gcap is faster btw :)

Tommy_TwoToes: We use TICK and Alerta for monitoring and alert management and
