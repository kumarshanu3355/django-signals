# README.md

##  Django Signals: Synchronous or Asynchronous?

### ✅ Answer:
By default, **Django signals execute synchronously**. 

This means that when a signal is triggered, the signal handler runs **before** the rest of the code continues.

The following code proves that behavior.

---

## 🧪 Python Code to Demonstrate Synchronous Signal

```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time

@receiver(post_save, sender=User)
def slow_signal_handler(sender, instance, **kwargs):
    print("Signal received, processing...")
    time.sleep(5)  # Simulate a slow operation
    print("Signal processing complete!")

# Creating a user to trigger the signal
new_user = User.objects.create(username="test_user", password="test123")
print("User creation complete!")
```

### 🧾 Output:
```
Signal received, processing...
(wait for 5 seconds...)
Signal processing complete!
User creation complete!
```

### ✅ Conclusion:
As you can see, the message **"User creation complete!"** is printed **only after** the signal handler finishes. 

This confirms that **Django signals are synchronous by default.**

---


