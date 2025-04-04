# README.md

##  Django Signals: Synchronous or Asynchronous?

### ✅ Answer:
By default, **Django signals execute synchronously**. 

This means that when a signal is triggered, the signal handler runs **before** the rest of the code continues.

The following code proves that behavior.

---

##  Python Code to Demonstrate Synchronous Signal
R
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

##  Do Django Signals Run in the Same Thread as the Caller?

### ✅ Answer:
Yes, by default, **Django signals run in the same thread** as the code that triggers them.

The following code shows that both the caller and the signal handler share the same thread ID.

---

##  Code to Prove Signal Runs in Same Thread

```python
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def signal_handler(sender, instance, **kwargs):
    print(f"[Signal] Running in thread ID: {threading.get_ident()}")

print(f"[Main] Running in thread ID: {threading.get_ident()}")

# Creating a user to trigger the signal
new_user = User.objects.create(username="thread_test_user", password="pass123")
```

###  Output Example:
```
[Main] Running in thread ID: 123456789
[Signal] Running in thread ID: 123456789
```

### ✅ Conclusion:
Both the main code and the signal handler output the **same thread ID**, proving that **Django signals run in the same thread as the caller by default.**

---

##  Do Django Signals Run in the Same Database Transaction as the Caller?

### ✅ Answer:
Yes, by default, **Django signals run within the same database transaction** as the code that triggers them.

The signal will only be committed to the database if the main transaction is committed successfully.

---

##  Code to Prove Signal Runs in Same Transaction

```python
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def signal_handler(sender, instance, **kwargs):
    print("Signal triggered for user:", instance.username)
    if instance.username == "rollback":
        raise Exception("Forcing rollback from signal")

try:
    with transaction.atomic():
        User.objects.create(username="rollback", password="123")
except Exception as e:
    print("Transaction rolled back due to:", e)

# Check if user was saved
print(User.objects.filter(username="rollback").exists())  # Should print False
```

###  Output Example:
```
Signal triggered for user: rollback
Transaction rolled back due to: Forcing rollback from signal
False
```

### ✅ Conclusion:
This proves that **if a signal handler raises an error, the entire transaction is rolled back** — meaning Django signals run within the same transaction as the caller.

---

 This behavior ensures data consistency unless you explicitly move logic outside the transaction.
