# Design patterns 

For wxpython there are a few modern ones to consider.

## [Pub Sub](https://dzone.com/articles/tutorial-on-wxpython-4-and-pubsub) 

Descendent of the message queue paradigm. Senders of messages are called publishers. We do not program the messages to be sent directly to specific "receivers" or "listener singleton" (also called "subscribers") Instead we categorize published messages into classes (often called topics) without knowledge of which subscribers get them. There may be zero or more subscribers.

AWS has [Pub/Sub messaging](https://aws.amazon.com/pub-sub-messaging/). Originally the beginning services with AWS to cater to [this model](https://aws.amazon.com/blogs/compute/building-scalable-applications-and-microservices-adding-messaging-to-your-toolbox/) was SNS (Simple Notification Service) and SQS (Simple Queueing Service), and when used together offers one deliver method of the pub/sub model via the cloud. The messages are typically in  XML, JSON, binary data, and so forth. Often we can also add optional attributes and metadata to a message with Enterprise messaging, and can be seen delivered with both UDP and TCP protocols. 

We use this model to broadcast asynchronous event notifications with endpoints that can offer software components to connect to the topic, and sometimes we see this called a message topic. This may be fanned out to multiple destinations as a broadcasted message in batches, with little or no queuing necessary. We will dig into this with docker and kubernetes after getting some apps going with wxPython. 

## Pub Sub and wxPython 4

We even have PyPubSub or PyDispatcher packages to help here specific to wxPython 4.

## [Observer Pattern](https://en.wikipedia.org/wiki/Observer_pattern)

Also a derivative of pub/sub