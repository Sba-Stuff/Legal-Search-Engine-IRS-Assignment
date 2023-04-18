@echo off
setlocal EnableDelayedExpansion

set "firstLine="
(for /F "delims=" %%a in (roul.txt) do (
   if not defined firstLine (
      set "firstLine=%%a"
   ) else (
      echo !firstLine! %%a
      set "firstLine="
   )
)) > finallist.txt