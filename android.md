# Android, uninstall bloatware / ads / junks / useless / optional

from https://forum.xda-developers.com/t/uninstall-bloatwares-no-root.4321387/

## Install & use

```sh
adb shell

# List packages
cmd package list packages


# Uninstall the application (remove the "package:" if you used the previous command to list them)
pm uninstall -k --user 0 <package-name>

# -k : Keep the data and cache directories around after package removal.
# --user 0: The user to disable

# Re-install an uninstalled package
cmd package install-existing <package-name>

# List all packages you uninstalled. Run it from a bash shell: not in adb shell
diff <(adb shell pm list packages) <(adb shell pm list packages -u) -n | grep ^package:
```

## List

```sh
pm uninstall -k --user 0 com.google.android.apps.googleassistant
pm uninstall -k --user 0 com.google.android.apps.subscriptions.red
pm uninstall -k --user 0 com.google.android.googlequicksearchbox
pm uninstall -k --user 0 com.android.browser                        # Mi Browser. It's a buggy unnecessary mess. Recommend you use other browsers like Chrome.

pm uninstall -k --user 0 cn.wps.xiaomi.abroad.lite # WPS Office. Has been flagged for years for malware. This was banned in India for a reason.

pm uninstall -k --user 0 com.ebay.carrier                # In case bloatware from Ebay is installed.
pm uninstall -k --user 0 com.facebook.services    # In case Facebook bloatware was preinstalled.
pm uninstall -k --user 0 com.facebook.system      # Also Facebook bloat.
pm uninstall -k --user 0 com.facebook.appmanager   # Also Facebook bloat.

pm uninstall -k --user 0 com.mi.globalbrowser      # Also part of Mi Browser.
pm uninstall -k --user 0 com.micredit.in                  # Mi Credit. Basically useless if you live outside India.
pm uninstall -k --user 0 com.mipay.wallet.in          # Part of Mi Credit.pm uninstall -k --user 0 com.miui.videoplayer      # Mi Video player. Uninstall if you prefer to use MX Player or VLC that actually support more formats.
pm uninstall -k --user 0 com.miui.cleanmaster     # Together with WPS Office, Cleaner Master was found to be affiliated with Cheetah Mobile, that included spyware and adware in their software.
pm uninstall -k --user 0 com.miui.hybrid                 # Found to be a data mining app that unnecesarily uses your phone's resources.
pm uninstall -k --user 0 com.miui.hybrid.accessory # Also a data mining app. Very recommend that you get rid of this.
pm uninstall -k --user 0 com.miui.micloudsync     # Include if you don't use Mi Cloud.
pm uninstall -k --user 0 com.miui.msa.global        # MSA. This is the main service that displays ads in Xiaomi phones. This is already removed in Xiaomi.EU.
pm uninstall -k --user 0 com.miui.notes                 # Include if you use other notes apps.
pm uninstall -k --user 0 com.miui.player                # Include if you don't use Xiaomi's music app.
pm uninstall -k --user 0 com.miui.weather2          # Include if you use other apps to get the weather like Google or Yahoo.

pm uninstall -k --user 0 com.xiaomi.midrop         # Breaks screen cast feature
pm uninstall -k --user 0 com.xiaomi.miplay_client  # Mi Play. This is an unnecessary process that hasn't really been used for years.
pm uninstall -k --user 0 com.xiaomi.glgm             # Mi Games. Very unncessary.
pm uninstall -k --user 0 com.xiaomi.mipicks        # Very unnecessary. Xiaomi's way to advertise their own apps.
pm uninstall -k --user 0 com.xiaomi.joyose           # Junk and safe to remove.
pm uninstall -k --user 0 com.xiaomi.payment       # Unless you live in China or India, Xiaomi's own payment service is redundant and unnecessary.

```
