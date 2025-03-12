RESTful Notification Forwarder

Overview

This project implements a RESTful web service that receives notifications via a POST interface and forwards them to a Slack channel based on their type. Notifications classified as Warning are forwarded, while those classified as Info are ignored.

Features

Accepts notifications via a POST request.

Filters notifications based on type.

Forwards Warning notifications to a Slack Channel.

Ignores Info notifications.
