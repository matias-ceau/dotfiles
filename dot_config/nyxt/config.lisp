(define-configuration buffer
  ((default-modes
    (pushnew 'nyxt/mode/vi:vi-normal-mode %slot-value%))))

(defvar *my-search-engines*
  (list
   '("google" "https://google.com/search?q=~a" "https://google.com")
   '("python3" "https://docs.python.org/3/search.html?q=~a"
     "https://docs.python.org/3")
   '("doi" "https://dx.doi.org/~a" "https://dx.doi.org/"))
  "List of search engines.")

(define-configuration web-buffer
  ((default-modes
    (pushnew 'nyxt/mode/blocker:blocker-mode %slot-value%))))

(define-configuration context-buffer
  "Go through the search engines above and `make-search-engine' out of them."
  ((search-engines
    (append
     (mapcar (lambda (engine) (apply 'make-search-engine engine))
             *my-search-engines*)
     %slot-default%))))

(defmethod initialize-instance :after
           ((interface password:keepassxc-interface)
            &key &allow-other-keys)
  "It's obviously not recommended to set master password here,
as your config is likely unencrypted and can reveal your password to someone
peeking at the screen."
  (setf (password:password-file interface)
          "/home/matias/.localdata/monkeypass/database.kdbx"
        (password:key-file interface) "/home/matias/notes/resources/georgeabitbol"
        ))

(define-configuration nyxt/mode/password:password-mode
  ((nyxt/mode/password:password-interface
    (make-instance 'password:keepassxc-interface))))

(define-configuration buffer
  ((default-modes
    (append (list 'nyxt/mode/password:password-mode) %slot-value%))))

(define-configuration browser
  ((theme (make-instance 'theme:theme 
			 :dark-p t
			 :background-color "#000000"
			 :on-background-color  "#ffffff"
			 :primary-color "#b7b5ac" 
			 :on-primary-color "#100f0f" 
			 :secondary-color "#403e3c" 
			 :on-secondary-color "#000000" 
			 :accent-color "#ad8301" 
			 :on-accent-color "#000000" 
			 :action-color "#ad8301" 
			 :success-color "#66800b" 
			 :warning-color "#dc322f"
			 :highlight-color "#d33682" 
			 :codeblock-color "#8b7ec8"
			 :text-color "#b7b5ac"
			 :contrast-text-color "#282726")
)))



;; (define-configuration prompt-buffer
;;   ((style (str:concat
;;            %slot-default%
;;            (cl-css:css
;;             '((body
;;                :background-color "#000000"
;;                :color "#808080")
;;               ("#prompt-area"
;;                :background-color "#000000")
;;               ;; The area you input text in.
;;               ("#input"
;;                :background-color "#ffffff")
;;               (".source-name"
;;                :color "#000000"
;;                :background-color "#575653")
;;               (".source-content"
;;                :background-color "#000000")
;;               (".source-content th"
;;                :border "1px solid black"
;;                :background-color "#000000")
;;               ;; The currently highlighted option.
;;               ("#selection"
;;                :background-color "#ad8301"
;;                :color "#000000")
;;               (.marked :background-color "#1c1b1a"
;;                        :font-weight "bold"
;;                        :color "#ffffff")
;;               (.selected :background-color "#000000"
;;                          :color "#ffffff")))))))

;; ;;; Panel buffers are the same in regards to style.
;; (define-configuration (internal-buffer panel-buffer)
;;   ((style
;;     (str:concat
;;      %slot-default%
;;      (cl-css:css
;;       '((body
;;          :background-color "#000000"
;;          :color "#878580")
;;         (hr
;;          :color "#1c1b1a")
;;         (a
;;          :color "#878580")
;;         (.button
;;          :color "#878580"
;;          :background-color "#575653")))))))
;;
;; ;;; Panel buffers are the same in regards to style.
;; (define-configuration (internal-buffer panel-buffer)
;;   ((style
;;     (str:concat
;;      %slot-default%
;;      (cl-css:css
;;       '((body
;;          :background-color "#000000"
;;          :color "#878580")
;;         (hr
;;          :color "#1c1b1a")
;;         (a
;;          :color "#878580")
;;         (.button
;;          :color "#878580"
;;          :background-color "#575653")))))))
